import pyodbc
from databaseConnection import dbConnect,dbCloseConnection, DBError

def main():
    try:
        # connecting to the database
        connection = dbConnect()

        dbCloseConnection(connection)
    except DBError as e:
        print(f"Error: {e}")

if (__name__ == '__main__'):
    main()
