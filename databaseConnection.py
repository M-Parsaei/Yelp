import os
from dotenv import load_dotenv
import pyodbc

class DBError(Exception):
    pass


def dbStartConnection() -> pyodbc.Connection:
    """
    starts a connection to the sql database.

    Returns:
        pyodbc.Connection: A connection object to the database.

    """

    # loading the env file
    load_dotenv()

    # getting the server name, password and user from environment file
    server_name = os.getenv("server_name")
    db_user = os.getenv("user_id")
    db_password = os.getenv("db_password")

    #connecting to db
    try:
        connection = pyodbc.connect('driver={SQL Server};'+f'server={server_name};\
                            uid={db_user};pwd={db_password}')
    except:
        raise DBError("failed to start the connection to database")
    
    return connection


def dbCloseConnection(connection: pyodbc.Connection):
    """
    stops the connection to the database.

    Args:
        connection (pyodbc.Connection): The pyodbc Connection to the db

    """
    try:
        connection.close()
        print("connection successfuly closed")
    except:
        raise DBError("failed to stop the connection from the database")