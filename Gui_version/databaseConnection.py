import os
from dotenv import load_dotenv
import pyodbc

class DBError(Exception):
    pass


class DBServer():

    def __init__(self):
        """
        starts a connection to the sql database.

        """

        # loading the env file
        load_dotenv()

        # getting the server name, password and user from environment file
        server_name = os.getenv("server_name")
        db_user = os.getenv("user_id")
        db_password = os.getenv("db_password")

        #connecting to db
        try:
            self.dbConnection = pyodbc.connect('driver={SQL Server};'+f'server={server_name};\
                                uid={db_user};pwd={db_password}')
            # making a cursor of db in order to executes queries
            self.dbCursor = self.dbConnection.cursor()
        except:
            raise DBError("failed to start the connection to database")
        
    def hmm(self):
        print("fuck")

    def dbCloseConnection(self):
        """
        stops the connection to the database.

        """
        try:
            self.dbConnection.close()
            print("connection successfuly closed")
        except:
            raise DBError("failed to stop the connection from the database")