-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema little_lemon_capstone
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema little_lemon_capstone
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `little_lemon_capstone` ;
USE `little_lemon_capstone` ;

-- -----------------------------------------------------
-- Table `little_lemon_capstone`.`Address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_capstone`.`Address` (
  `addressId` INT NOT NULL,
  `streetNo` INT NOT NULL,
  `street` VARCHAR(45) NULL,
  `city` VARCHAR(45) NULL,
  `zip` INT NULL,
  `state` VARCHAR(2) NULL,
  PRIMARY KEY (`addressId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `little_lemon_capstone`.`Customers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_capstone`.`Customers` (
  `customerId` INT NOT NULL,
  `firstName` VARCHAR(45) NOT NULL,
  `LastName` VARCHAR(45) NOT NULL,
  `phone` VARCHAR(45) NULL,
  `email` VARCHAR(45) NOT NULL,
  `addressId` INT NOT NULL,
  PRIMARY KEY (`customerId`),
  INDEX `customer_address_Id_idx` (`addressId` ASC) VISIBLE,
  CONSTRAINT `customer_address_Id`
    FOREIGN KEY (`addressId`)
    REFERENCES `little_lemon_capstone`.`Address` (`addressId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `little_lemon_capstone`.`Staff`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_capstone`.`Staff` (
  `staffId` INT NOT NULL,
  `firstName` VARCHAR(45) NULL,
  `lastName` VARCHAR(45) NULL,
  `phone` VARCHAR(45) NULL,
  `role` VARCHAR(45) NULL,
  `salary` INT NULL,
  PRIMARY KEY (`staffId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `little_lemon_capstone`.`Bookings`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_capstone`.`Bookings` (
  `bookingId` INT NOT NULL,
  `customerId` INT NOT NULL,
  `staffId` INT NOT NULL,
  `date` DATETIME NOT NULL,
  `tableNo` INT NOT NULL,
  `partySize` INT NOT NULL,
  PRIMARY KEY (`bookingId`),
  INDEX `booking_customer_id_idx` (`customerId` ASC) VISIBLE,
  INDEX `booking_staff_id_idx` (`staffId` ASC) VISIBLE,
  CONSTRAINT `booking_customer_id`
    FOREIGN KEY (`customerId`)
    REFERENCES `little_lemon_capstone`.`Customers` (`customerId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `booking_staff_id`
    FOREIGN KEY (`staffId`)
    REFERENCES `little_lemon_capstone`.`Staff` (`staffId`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `little_lemon_capstone`.`Orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_capstone`.`Orders` (
  `orderId` INT NOT NULL,
  `date` DATETIME NOT NULL,
  `customerId` INT NOT NULL,
  `staffId` INT NOT NULL,
  `bookingId` INT NULL,
  `type` VARCHAR(45) NOT NULL,
  `totalPrice` INT NOT NULL,
  PRIMARY KEY (`orderId`),
  INDEX `orders_booking_id_idx` (`bookingId` ASC) VISIBLE,
  INDEX `orders_staff_id_idx` (`staffId` ASC) VISIBLE,
  INDEX `orders_customer_idx` (`customerId` ASC) VISIBLE,
  CONSTRAINT `orders_booking_id`
    FOREIGN KEY (`bookingId`)
    REFERENCES `little_lemon_capstone`.`Bookings` (`bookingId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `orders_staff_id`
    FOREIGN KEY (`staffId`)
    REFERENCES `little_lemon_capstone`.`Staff` (`staffId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `orders_customer`
    FOREIGN KEY (`customerId`)
    REFERENCES `little_lemon_capstone`.`Customers` (`customerId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `little_lemon_capstone`.`Deliveries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_capstone`.`Deliveries` (
  `deliveryId` INT NOT NULL,
  `orderId` INT NOT NULL,
  `status` VARCHAR(45) NOT NULL,
  `timeFufilled` DATETIME NULL,
  PRIMARY KEY (`deliveryId`),
  INDEX `deliveries_order_id_idx` (`orderId` ASC) VISIBLE,
  CONSTRAINT `deliveries_order_id`
    FOREIGN KEY (`orderId`)
    REFERENCES `little_lemon_capstone`.`Orders` (`orderId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `little_lemon_capstone`.`Menu`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_capstone`.`Menu` (
  `menuId` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `cuisine` VARCHAR(45) NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `unitPrice` DECIMAL(5,2) NOT NULL,
  PRIMARY KEY (`menuId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `little_lemon_capstone`.`menu_orders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `little_lemon_capstone`.`menu_orders` (
  `orderId` INT NOT NULL,
  `menuId` INT NOT NULL,
  `quantity` INT NOT NULL,
  INDEX `intermediary_orderId_idx` (`orderId` ASC) VISIBLE,
  INDEX `intermediary_menuId_idx` (`menuId` ASC) VISIBLE,
  CONSTRAINT `intermediary_orderId`
    FOREIGN KEY (`orderId`)
    REFERENCES `little_lemon_capstone`.`Orders` (`orderId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `intermediary_menuId`
    FOREIGN KEY (`menuId`)
    REFERENCES `little_lemon_capstone`.`Menu` (`menuId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
