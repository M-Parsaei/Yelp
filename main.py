import pyodbc
from databaseConnection import dbStartConnection,dbCloseConnection, DBError
import authenticate,contorllers

def main():
    try:
        # connecting to the database
        connection = dbStartConnection()

        # making a cursor of db in order to executes queries
        dbCursor = connection.cursor()

        #Asking user for their user_id 
        #user_id = input("Please Enter your user_id in order to login: \n")
        #checking if the user_id is valid to login
        # if not authenticate.login(user_id,dbCursor):
        #     print("Not logged IN...")
        #else: 
        #    print("Logged In...")

        contorllers.searchBusiness(filter={"name":"chrysler"},
                                   cursor=dbCursor,
                                   connection=connection)


        dbCloseConnection(connection)
    except DBError as e:
        print(f"Error: {e}")

if (__name__ == '__main__'):
    main()
