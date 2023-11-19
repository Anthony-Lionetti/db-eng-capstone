OrderView = """CREATE VIEW OrdersView AS
        SELECT o.orderId, SUM(mo.quantity) as Quantity, SUM(mo.quantity * m.unitPrice) as Cost
        FROM Orders as o
        JOIN menu_orders as mo
        on o.orderId = mo.orderId
        JOIN Menu as m
        on mo.menuId = m.menuId
        GROUP BY o.orderId;"""

Over90Orders = """CREATE VIEW OverNinetyOrders AS
        SELECT c.CustomerId, CONCAT(c.firstName, " ", c.lastName) AS FullName, o.orderId, o.type, SUM(mo.quantity * m.unitPrice) as Cost
        FROM Orders as o
        JOIN customers as c
            ON o.customerId = c.customerId
        JOIN menu_orders as mo
            ON o.orderId = mo.orderId
        JOIN Menu as m
            ON mo.menuId = m.menuId
        GROUP BY o.orderId
        HAVING SUM(mo.quantity * m.unitPrice) > 90;"""

PopularItems = """
        CREATE VIEW PopularItems AS 
        SELECT name
        FROM menu
        WHERE menuId = ANY(
            SELECT menuId
            FROM menu_orders 
            GROUP BY menuId
            HAVING COUNT(OrderId) > 3);
            """
GetMaxQuantity = """
        CREATE PROCEDURE GetMaxQuantity()
        BEGIN
            SELECT SUM(quantity) as 'Max Order Size'
            FROM menu_orders
            GROUP BY orderId
            ORDER BY SUM(quantity) DESC
            LIMIT 1;
        END"""

GetCustomerPreppared = """
        SELECT c.customerId, o.orderId, SUM(mo.quantity) as Quantity, SUM(unitPrice) AS Cost
        FROM customers as c
        JOIN orders as o
            ON c.customerId = o.customerId
        JOIN menu_orders as mo
            ON o.orderId = mo.orderId
        JOIN menu as m
            ON m.menuId = mo.menuId
        GROUP BY o.orderId
        HAVING c.customerId = %s """

CancelOrder = """
                CREATE PROCEDURE CancelOrder(IN order_id INT, OUT message VARCHAR(100))
                BEGIN 
                    DELETE FROM Orders 
                    WHERE orderId = order_id;
                    SET message := CONCAT("Order ", order_id, " is cancelled");
                END
                """
