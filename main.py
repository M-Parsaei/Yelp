import pyodbc
from databaseConnection import dbStartConnection,dbCloseConnection, DBError
import authenticate,contorllers
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
import sys
from userInterface.login_page import Ui_Form

# a boolean that defines whether the program should end or not 
is_program_over = False

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


        #setting up the login user interface 
        app = QApplication(sys.argv)
        Form = QtWidgets.QWidget()
        ui = Ui_Form()
        ui.setupUi(Form)
        Form.show()
        


        '''result = contorllers.searchTable(filter={"name":"john"},
                                   tableName="user_yelp",
                                   cursor=dbCursor)

        print(result)'''
        sys.exit(app.exec_())

    except DBError as e:
        print(f"Error: {e}")


def endProgram(connection: pyodbc.Connection):
    dbCloseConnection(connection)

if (__name__ == '__main__'):
    main()
