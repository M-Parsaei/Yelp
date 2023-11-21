import pyodbc
from databaseConnection import dbConnect

def main():
    try:
        # connecting to the database
        connection = dbConnect()
    except:
        print("Cound not connect to the database")

if (__name__ == '__main__'):
    main()
