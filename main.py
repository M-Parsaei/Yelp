import pyodbc
from databaseConnection import DBServer, DBError
import authenticate,contorllers
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets
import sys
from userInterface.login_page import Ui_Form

# a boolean that defines whether the program should end or not 
is_program_over = False
databaseRef = None

def main():
    try:
        databaseRef = DBServer()
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


def endProgram(databaseRef: DBServer):
    databaseRef.dbCloseConnection()

if (__name__ == '__main__'):
    main()
