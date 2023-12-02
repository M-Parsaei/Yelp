import os
from dotenv import load_dotenv
import pyodbc
import queriesSkelton

class DBError(Exception):
    pass


class DBServer():

    def __init__(self):
        """
        starts a connection to the sql database.

        """

        # loading the env file
        load_dotenv()

        # getting the server name, password and user from environment file
        server_name = os.getenv("server_name")
        db_user = os.getenv("user_id")
        db_password = os.getenv("db_password")

        #connecting to db
        try:
            self.dbConnection = pyodbc.connect('driver={SQL Server};'+f'server={server_name};\
                                uid={db_user};pwd={db_password}')
            # making a cursor of db in order to executes queries
            self.dbCursor = self.dbConnection.cursor()
        except:
            raise DBError("failed to start the connection to database")
        

    def searchTable(self,filter: dict, tableName: str,)-> list:
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
            if key not in ("stars", "average_stars","review_count"):
                query = query + f"{key} = ?"
            else:
                query = query + f"{key} >= ?"

            #if the value was string, then add its lowercase to list
            # in order to have a case-insenstive search
            queryParams.append(value.lower() if type(value)=="str" else value)

            index += 1

        # finishs the query with ;
        query = query + " ;"

        #executes the query and fetch all matching records as a list
        result = self.dbCursor.execute(query,queryParams).fetchall()

        return result

    def login(self,id: str) -> bool:
        """
        returns true if there exists a tuple in user_yelp table 
        such that the id attribute of tupple is same as id argument

        Returns:
            bool: true if the id exists as a Id attrbuite in user_yelp table

        Args:
            id (str): The user ID

        """

        id = id.strip()

        check_user_valid_query = "SELECT * \n FROM user_yelp AS U \n WHERE U.user_id = ? "
        
        
        result = self.dbCursor.execute(check_user_valid_query,[id]).fetchone()
        #print(id)
        #print(check_user_valid_query)
        #print(result)
        if result is None:
            # there is no such user_id in database, return false
            # as they are not allowed to login
            return False
        #otherwise the user_id was in database, so return true to approve login
        return True
    
    def dbCloseConnection(self):
        """
        stops the connection to the database.

        """
        try:
            self.dbConnection.close()
            print("connection successfuly closed")
        except:
            raise DBError("failed to stop the connection from the database")