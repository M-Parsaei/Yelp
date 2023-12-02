from colorama import Fore, Back, Style,init


def askTask() -> str:
    print("For using any of the feature, please type the corresponding number:")
    print("1- Searching for business (type 1)")
    print("2- Searching for users (type 2)")
    print("3- Add a friend (type 3)")
    print("4- Add a review for a business (type 4)")
    return input("Please type the number of task you wish or type exit for quitting program: -> ")

def askUserID() -> bool:
    is_user_logged_in = False
    while(not is_user_logged_in):
        user_id = input("Please Enter your user_id to log in: -> ")
        if(user_id == 'exit'):
            return False
        is_user_logged_in = login(user_id.strip())
        if (not is_user_logged_in):
            print(Fore.RED + Back.LIGHTWHITE_EX + "Invalid Credential")  
        else:
            print(Fore.GREEN + Back.LIGHTWHITE_EX + "Logged In successfuly.")
            return True


def login(id: str) -> bool:
    """
    returns true if there exists a tuple in user_yelp table 
    such that the id attribute of tupple is same as id argument

    Returns:
        bool: true if the id exists as a Id attrbuite in user_yelp table

    Args:
        id (str): The user ID

    """

    from main import databaseRef

    check_user_valid_query = 'SELECT user_id\
                            FROM user_yelp AS U\
                            WHERE U.user_id = ?'
    
    
    result = databaseRef.dbCursor.execute(check_user_valid_query,[id]).fetchone()
    if result is None:
        # there is no such user_id in database, return false
        # as they are not allowed to login
        return False
    #otherwise the user_id was in database, so return true to approve login
    return True
