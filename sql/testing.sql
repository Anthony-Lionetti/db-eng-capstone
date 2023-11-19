CREATE PROCEEDURE CancelOrder(IN order_id INT)
BEGIN 
    DELETE FROM Orders 
    WHERE orderId = order_id;
    SELECT CONCAT("Order ", order_id, " is cancelled") AS Confirmation;
END