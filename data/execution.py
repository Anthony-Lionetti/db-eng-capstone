import mysql.connector
from mysql.connector import ProgrammingError
from data.insert_queries import insert_statements
from data.task_queries import OrderView, Over90Orders, PopularItems, GetMaxQuantity, GetCustomerPreppared, CancelOrder

# for typhinting purposes #
from mysql.connector.cursor import MySQLCursor, MySQLCursorPrepared
from mysql.connector import MySQLConnection


## Create Connection ##
def init_database():
    """
    Purpose: Used to connect to Local DB create DB and populate it with data
    Return:
        tuple (cnx, cursor) - A tuple with mysql connection and a cursor respectively
    """
    cnx = mysql.connector.connect(user=input("Database username"),
                                  password=input("Database password"),
                                  host='127.0.0.1'
                                  )
    ## Create a cursor object ##
    cursor = cnx.cursor()
    prep_cursor = cnx.cursor(prepared=True)
    return (cnx, cursor, prep_cursor)

## Insert Data ##


def insert_data(cnx: MySQLConnection, cursor: MySQLCursor) -> None:
    """
    Purpose: To insert test data for the 
    """
    try:
        cursor.execute("USE little_lemon_capstone;")
        print("Now using little_lemon_capstone")

    except ProgrammingError as err:
        print("Creating little_lemon_capstone")
        cursor.execute("CREATE DATABASE little_lemon_capstone")
        cursor.execute("USE little_lemon_capstone;")

        print("Creating Tables")
        with open('your_sql_script.sql', 'r') as file:
            sql_script = file.read()
        print("Executing sql script")
        statements = [s.strip() for s in sql_script.split(';') if s.strip()]
        for statement in statements:
            cursor.execute(statement)
        print("Execution Finished")
        cnx.commit()

    #################
    ## Insert Data ##
    #################
    try:
        for statement in insert_statements:
            cursor.execute(statement)
            cnx.commit()
    except:
        print("Check if Data is Already Added")


def run_views(cursor: MySQLCursor) -> (list, list, list):
    """
    Purpose: To create OrdersView, OverNinetyOrders, & PupularItems view responses;
    Arg:
        cursor - MySQL connector cursor object
    Returns:
        tuple of lists - Each list is the query results from OrdersView, OverNinetyOrders, & PupularItems respectively
    """
    # Virtual Table for # of items & cost for each order #
    cursor.execute("DROP VIEW IF EXISTS OrdersView;")
    cursor.execute(OrderView)
    cursor.execute("Select * from OrdersView;")
    order_views = cursor.fetchall()
    # END TASK 1 #

    # Getting all orders that have a value of Over 90 #
    cursor.execute("DROP VIEW IF EXISTS OverNinetyOrders;")
    cursor.execute(Over90Orders)

    cursor.execute("Select * from OverNinetyOrders;")
    over90orders = cursor.fetchall()
    # END TASK 2 #

    # Get menu itemds that are in 3 or more orders using subquery #
    cursor.execute("DROP VIEW IF EXISTS PopularItems;")
    cursor.execute(PopularItems)
    cursor.execute("Select * FROM PopularItems;")
    popular_items = cursor.fetchall()
    # End Task 3 #

    return (order_views, over90orders, popular_items)


def run_proceedures(cursor: MySQLCursor):
    cursor.execute("DROP PROCEDURE IF EXISTS GetMaxQuantity;")
    cursor.execute(GetMaxQuantity)
    cursor.execute("DROP PROCEDURE IF EXISTS CancelOrder;")
    cursor.execute(CancelOrder)


def call_procedure(cursor: MySQLCursor, name: str, args: tuple = ()) -> list:
    cursor.callproc(name, args)
    query = []
    for res in cursor.stored_results():
        query.append(res.fetchall())

    return query


def run_prepared_statement(prep_cursor: MySQLCursorPrepared, c_id: tuple) -> list:
    prep_cursor.execute(
        GetCustomerPreppared,
        c_id
    )

    return prep_cursor.fetchall()
