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
    if result:
        for item in result:
            print(item)
    else:
        print("There are no business matching your filters.")


def searchUsers(databaseRef: DBServer):
    print("Please enters the filters,\n"
           "if you don't want to filter users by any of the following option, type N/A for that option")
    filterDict={}

    name = input("name of user: -> ")
    minStar = input("Minimum average stars: -> ")
    minCount = input("Minimum review counts: -> ")

    if minStar.lower() != "n/a" :
        filterDict["average_stars"] = float(minStar)
    if minCount.lower() != "n/a" :
        filterDict["review_count"] = int(minCount)
    if name.lower() != "n/a" :
        filterDict["name"] = name

    result = databaseRef.searchTable(filter=filterDict,tableName="user_yelp")
    if result:
        for item in result:
            print(item)
    else:
        print("There are no users matching your filters.")

def addFriend(databaseRef: DBServer):
    print("Please type the id of person you want to add as friend")
    print("Or type cancel to quit Adding friend task")
    user_id = input("friend user id -> ")
    if user_id=="cancel":
        return 
    else:
        databaseRef.makeFriend(friend_id=user_id)

def addReview():
    pass