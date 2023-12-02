import pyodbc
from main import databaseRef

def login(id: str) -> bool:
    """
    returns true if there exists a tuple in user_yelp table 
    such that the id attribute of tupple is same as id argument

    Returns:
        bool: true if the id exists as a Id attrbuite in user_yelp table

    Args:
        id (str): The user ID

    """

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
