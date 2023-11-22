import pyodbc


def searchBusiness(filter: dict, 
                   cursor: pyodbc.Cursor)-> list:
    """
    returns the list of tuples in Business table which 
    matches the searching filter

    Returns:
        list: list of tuples

    Args:
        filter (dict): The filtering dictionary, for example {"name":"KFC","star":5} 
        if wants to filter only business with KFC as their name and have 5 star rating

        cursor (pyodbc.Cursor): The pyodbc Cursor in order to execute a query
        to find all of the matching business from the table
    """

    # the skelton of the query to find matching tuples
    # from business table
    query = (f"SELECT *"
            "FROM business AS B "
            "WHERE ")
    
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

    #executes the query and fetch all matching records as a list
    result = cursor.execute(query,queryParams).fetchall()

    return result



def searchUser():
    pass

def addFriends():
    pass

def addReview():
    pass