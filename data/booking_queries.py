CheckBooking = """
            CREATE PROCEDURE CheckBooking()
            BEGIN
               SELECT bookingId as "Booking #", date as 'Booking Date', tableNo as "Table Number", customerId as "Customer ID"
               FROM Bookings;
            END
            """

AddValidBooking = """
            CREATE PROCEDURE AddValidBooking()
            BEGIN
               
            END
"""


AddBooking = """
            CREATE PROCEDURE AddValidBooking()
            BEGIN
               
            END
"""
