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
    order = int(input("order by: -> "))


    result = databaseRef.searchTable(filter=filterDict,tableName="business")
    print("*************************************************\n")
    print("result is : \n ")

    if result:
        if (order == 1):
            # TODO to fix the star sorting
            result = sorted(result, key=lambda x: x[5])
        elif (order == 2):
            result = sorted(result, key=lambda x: x[3])
        else:
            result = sorted(result, key=lambda x: x[1])

        index = 1
        for item in result:
            print(f"{index}- \n\t Business ID: {item[0]} \n\t Name: {item[1]}"
                f"\n\t Address: {item[2]} \n\t City: {item[3]} \n\t Rating(# of stars): {item[5]} \n")
            index += 1
    else:
        print("There are no business matching your filters.")

    print("*************************************************\n")


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