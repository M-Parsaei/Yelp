from databaseConnection import DBServer, DBError
from colorama import just_fix_windows_console,Fore, Back,init
from authenticate import askUserID, askTask
from helpers import searchBusiness,searchUsers,addFriend,addReview

databaseRef = DBServer()
just_fix_windows_console()
init(autoreset=True)

def main():
    try:

        global databaseRef


        # a boolean that defines whether the program should end or not 
        is_program_over = False

        print(Back.WHITE + Fore.GREEN + "welcome to Yelp - command Line version")  
        print("For exiting the program, type exit in any stage of program")     

        is_success_login = askUserID(databaseRef)
        if (not is_success_login):
            endProgram()

        while(not is_program_over):
            user_input = askTask().strip()
            if(user_input=="exit"):
                is_program_over = True
                endProgram()
            elif (user_input=="1"):
                searchBusiness(databaseRef)
            elif (user_input=="2"):
                searchUsers(databaseRef)
            elif (user_input=="3"):
                addFriend(databaseRef)
            elif (user_input=="4"):
                addReview(databaseRef)
            else:
                print("Invalid task number, please try again")

        endProgram()

    
    except DBError as e:
        print(f"Error: {e}")


def endProgram():

    global databaseRef

    databaseRef.dbCloseConnection()
    print(Fore.GREEN + "User exited the program")
    exit(0)

if (__name__ == '__main__'):
    main()
