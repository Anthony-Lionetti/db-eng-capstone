CheckBooking = """
            CREATE PROCEDURE CheckBooking()
            BEGIN
               SELECT bookingId as "Booking #", date as 'Booking Date', tableNo as "Table Number", customerId as "Customer ID"
               FROM Bookings;
            END
            """

AddBooking = """
            CREATE PROCEDURE AddBooking(IN booking_Id int, IN customer_Id int,  IN staff_Id int, IN date_input DATETIME, IN table_no int, In party_size int)
            BEGIN
               INSERT INTO Bookings (bookingId, customerId, staffId, date, tableNo, partySize)
               VALUES (booking_Id, customer_Id, staff_Id, date_input, table_no, party_size);
               SELECT * FROM Bookings WHERE bookingId = booking_id;
            END
         """

UpdateBooking = """
            CREATE PROCEDURE UpdateBooking(IN booking_id int, IN date_input DATETIME)
            BEGIN
               UPDATE Bookings
               SET date = date_input
               WHERE bookingId = booking_id;
               SELECT * FROM Bookings WHERE bookingId = booking_id;
            END
         """


CancelBooking = """
            CREATE PROCEDURE CancelBooking(IN booking_id int)
            BEGIN
               DELETE FROM Bookings
               WHERE bookingId  = booking_id;
               SELECT CONCAT("Booking Id: ", booking_id, " deleted successfully");
            END
         """
