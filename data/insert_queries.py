add_addresses = """
INSERT INTO Address (addressId, streetNo, street, city, zip, state)
VALUES (1, 123, 'Maple Street', 'Los Angeles', 90001, 'CA'),
(2, 456, 'Oak Avenue', 'San Francisco', 94102, 'CA'),
(3, 789, 'Pine Road', 'San Diego', 92103, 'CA'),
(4, 101, 'Elm Lane', 'Sacramento', 94203, 'CA')
"""


add_customers = """
INSERT INTO Customers (customerId, firstName, lastName, phone, email, addressId)
VALUES (1, 'John', 'Doe', '123-456-7890', 'john.doe@example.com', 1),
(2, 'Jane', 'Smith', '234-567-8901', 'jane.smith@example.com', 2),
(3, 'Mike', 'Brown', '345-678-9012', 'mike.brown@example.com', 3),
(4, 'Lisa', 'White', '456-789-0123', 'lisa.white@example.com', 4),
(5, 'Matt', 'Smith', '234-567-8111', 'matt.smith@example.com', 2),
(6, 'David', 'White', '456-789-2345', 'david.White@example.com', 4)
"""

add_staff = """
INSERT INTO Staff (staffId, firstName, lastName, phone, role, salary)
VALUES (1, 'Alex', 'Gordon', '111-222-3333', 'Chef', 65000),
(2, 'Sarah', 'Miller', '222-333-4444', 'Host', 50000),
(3, 'Jake', 'Taylor', '333-444-5555', 'Driver', 30000),
(4, 'Mia', 'Brown', '444-555-6666', 'Driver', 30000),
(5, 'Chris', 'White', '555-666-7777', 'Waiter', 35000),
(6, 'Olivia', 'Davis', '666-777-8888', 'Waiter', 35000),
(7, 'Dave', 'Keys', '267-373-4774', 'Host', 45000)
"""

add_bookings = """
INSERT INTO Bookings (bookingId, customerId, staffId, date, tableNo, partySize)
VALUES (1, 1, 2, '2023-11-20', 5, 2),
(2, 2, 7, '2023-11-21', 3, 4),
(3, 3, 7, '2023-11-22', 1, 3),
(4, 4, 2, '2023-11-23', 6, 2)
"""

add_menu = """
INSERT INTO Menu (menuId, name, cuisine, type, unitPrice)
VALUES (1, 'Tzatziki Dip', 'Greek', 'Appetizer', 7.99),
(2, 'Bruschetta', 'Italian', 'Appetizer', 8.99),
(3, 'Dolmades', 'Greek', 'Appetizer', 6.99),
(4, 'Caprese Salad', 'Italian', 'Appetizer', 7.5),
(5, 'Moussaka', 'Greek', 'Entree', 15.99),
(6, 'Lasagna', 'Italian', 'Entree', 16.99),
(7, 'Souvlaki', 'Greek', 'Entree', 14.99),
(8, 'Risotto', 'Italian', 'Entree', 15.5),
(9, 'Gyros', 'Greek', 'Entree', 17.99),
(10, 'Ravioli', 'Italian', 'Entree', 18.5),
(11, 'Baklava', 'Greek', 'Dessert', 5.99),
(12, 'Tiramisu', 'Italian', 'Dessert', 6.99),
(13, 'Galaktoboureko', 'Greek', 'Dessert', 5.5),
(14, 'Panna Cotta', 'Italian', 'Dessert', 6.5),
(15, 'Ouzo', 'Greek', 'Drink', 3.99),
(16, 'Limoncello', 'Italian', 'Drink', 4.99),
(17, 'Greek Coffee', 'Greek', 'Drink', 3.5),
(18, 'Espresso', 'Italian', 'Drink', 4.5)
"""

add_orders = """
INSERT INTO Orders (orderId, date, customerId, staffId, bookingId, type, totalPrice)
VALUES  (1, '2023-11-20', 1, 5, 1, "Booking", 121),
(2, '2023-11-21', 2, 6, 2, "Booking", 84),
(3, '2023-11-22', 3, 5, 3, "Booking", 35),
(4, '2023-11-16', 4, 4, NULL, "Delivery", 65),
(5, '2023-11-17', 5, 3, NULL, "Delivery", 70),
(6, '2023-11-18', 6, 3, NULL, "Delivery", 55),
(7, '2023-11-19', 1, 4, NULL, "Delivery", 89),
(8, '2023-11-23', 4, 6, NULL, "Walk-in", 57)
"""

add_deliveries = """
INSERT INTO Deliveries (deliveryId, orderId, status, timeFufilled)
VALUES (1, 4, 'Preparing', NULL),
(2, 5, 'In Route', NULL),
(3, 6, 'Delivered', '2023-11-16 14:00:00'),
(4, 7, 'Preparing', NULL)
"""

add_menu_orders = """
INSERT INTO menu_orders (orderId, menuId, quantity)
VALUES (1, 12, 3),
(1, 15, 1),
(1, 11, 2),
(1, 4, 3),
(1, 2, 3),
(2, 15, 3),
(2, 10, 2),
(2, 2, 2),
(2, 11, 1),
(2, 4, 1),
(2, 12, 2),
(3, 4, 2),
(3, 11, 3),
(3, 13, 1),
(3, 7, 2),
(4, 7, 3),
(4, 5, 1),
(4, 9, 1),
(4, 2, 2),
(5, 16, 1),
(5, 15, 3),
(5, 13, 2),
(5, 3, 1),
(6, 7, 1),
(6, 18, 1),
(6, 11, 3),
(7, 16, 3),
(7, 13, 3),
(7, 1, 1),
(8, 2, 3),
(8, 17, 3),
(8, 8, 1),
(8, 5, 2),
(8, 13, 1),
(8, 1, 1),
(8, 4, 3)
"""

insert_statements = [add_addresses,
                     add_customers,
                     add_staff,
                     add_bookings,
                     add_menu,
                     add_orders,
                     add_deliveries,
                     add_menu_orders]
