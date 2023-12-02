from colorama import Fore, Back, Style,init
from databaseConnection import DBServer

def askTask() -> str:
    print("For using any of the feature, please type the corresponding number:")
    print("1- Searching for business (type 1)")
    print("2- Searching for users (type 2)")
    print("3- Add a friend (type 3)")
    print("4- Add a review for a business (type 4)")
    return input("Please type the number of task you wish or type exit for quitting program: -> ")

def askUserID(databaseRef: DBServer) -> bool:
    is_user_logged_in = False
    while(not is_user_logged_in):
        user_id = input("Please Enter your user_id to log in: -> ")
        if(user_id == 'exit'):
            return False
        is_user_logged_in = databaseRef.login(user_id.strip())
        if (not is_user_logged_in):
            print(Fore.RED + Back.LIGHTWHITE_EX + "Invalid Credential")  
        else:
            print(Fore.GREEN + Back.LIGHTWHITE_EX + "Logged In successfuly.")
            return True

