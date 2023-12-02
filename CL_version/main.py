import pyodbc
from databaseConnection import DBServer, DBError
import authenticate,contorllers
from colorama import just_fix_windows_console,Fore, Back, Style,init

# a boolean that defines whether the program should end or not 
is_program_over = False
databaseRef = DBServer()

just_fix_windows_console()
init(autoreset=True)

def main():
    try:


        print(Back.WHITE + Fore.GREEN + "welcome to Yelp - command Line version")  
        print("For exiting the program, type exit in any stage of program")     


        authenticate.askUserID()

        print("For using any of the feature, please type the corresponding number:")
        print("1- Searching for business (type 1)")
        print("2- Searching for users (type 2)")
        print("3- Add a friend (type 3)")
        print("4- Add a review for a business (type 4)")
        input("Please type the number of task you wish or type exit for quitting program: ")

        '''result = contorllers.searchTable(filter={"name":"john"},
                                   tableName="user_yelp",
                                   cursor=dbCursor)

        print(result)'''

    except DBError as e:
        print(f"Error: {e}")


def endProgram():
    databaseRef.dbCloseConnection()
    print("User exited the program")
    exit(0)

if (__name__ == '__main__'):
    main()
