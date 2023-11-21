import pyodbc

def login(id: str,cursor: pyodbc.Cursor) -> bool:

    check_user_valid_query = 'SELECT user_id\
                            FROM user_yelp AS U\
                            WHERE U.user_id = ?'
    result = cursor.execute(check_user_valid_query,[id]).fetchone()
    if result is None:
        # there is no such user_id in database, return false
        # as they are not allowed to login
        return False
    #otherwise the user_id was in database, so return true to approve login
    return True
