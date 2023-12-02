from databaseConnection import DBServer

def searchBusiness(databaseRef: DBServer):
    print("Please enters the filters,\n"
           "if you don't filter business by any of the following option, type N/A for that option")
    filterDict={}


    minStar = input("Minimum number of business stars: -> ")
    city = input("city of business: -> ")
    name = input("name of business: -> ")

    if minStar.lower() != "n/a" :
        filterDict["stars"] = float(minStar)
    if city.lower() != "n/a" :
        filterDict["city"] = city
    if name.lower() != "n/a" :
        filterDict["name"] = name
    
    print("Order results by:\n"
          "type 1 to order by stars\n"
          "type 2 to order by city \n"
          "type 3 to order by name \n")
    order = input("order by: -> ")


    result = databaseRef.searchTable(filter=filterDict,tableName="business")
    print("result is : \n ")
    for item in result:
        print(item)


def searchUsers():
    pass

def addFriend():
    pass

def addReview():
    pass