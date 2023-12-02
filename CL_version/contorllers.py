import pyodbc
import queriesSkelton

def searchTable(filter: dict, tableName: str,)-> list:
    """
    returns the list of tuples in a table which 
    matches the searching filter

    Returns:
        list: list of tuples

    Args:
        filter (dict): The filtering dictionary, for example {"name":"KFC","stars":5} 
        if wants to filter only business with KFC as their name and have 5 star rating

        tableName (str): the name of the table which searchTable runs the query on

    """

    print("the filtering is ")
    print(filter)
    try:
        # getting the skelton of the search query 
        # for a table which its name was provided from tableName,
        # from the skeletonLists dict
        query = queriesSkelton.skeletonLists[tableName]
    except:
        # if there was no query for that table
        # then return empty list 
        print("Invalid table name")
        return []
    
    # queryParams is a list of filtering values 
    queryParams = []

    index = 0
    for key,value in filter.items():
        # add "AND" between the comparioson conditions in the WHERE clause
        query = query + " AND " if index != 0 else query

        # add ? as the value because we will add the value 
        # in the queryParams instead and pass this list
        # to cursor.execute 
        query = query + f"{key} = ?"

        #if the value was string, then add its lowercase to list
        # in order to have a case-insenstive search
        queryParams.append(value.lower() if type(value)=="str" else value)

        index += 1

    # finishs the query with ;
    query = query + " ;"

    from main import databaseRef
    #executes the query and fetch all matching records as a list
    result = databaseRef.dbCursor.execute(query,queryParams).fetchall()

    return result



def searchUser(filter: dict, 
               cursor: pyodbc.Cursor)->list:
   pass


def addFriends():
    pass

def addReview():
    pass