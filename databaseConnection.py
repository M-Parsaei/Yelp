import os
from dotenv import load_dotenv
import pyodbc


def dbConnect():
    # loading the env file
    load_dotenv()

    # getting the server name, password and user from environment file
    server_name = os.getenv("server_name")
    db_user = os.getenv("user_id")
    db_password = os.getenv("db_password")

    #connecting to db

    connection = pyodbc.connect('driver={SQL Server};'+f'server={server_name};\
                        uid={db_user};pwd={db_password}')
    
    return connection