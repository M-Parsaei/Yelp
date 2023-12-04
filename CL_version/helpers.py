from databaseConnection import DBServer
from colorama import Fore, Back, Style,init


def searchBusiness(databaseRef: DBServer):
    print("Please enters the filters,\n"
           "if you don't filter business by any of the following option, type N/A for that option")
    filterDict={}


    minStar = input("Minimum number of business stars: -> ")
    city = input("city of business: -> ")
    name = input("name of business: -> ")

    num_not_n_a_filters = 0
    if minStar.lower() != "n/a" :
        num_not_n_a_filters += 1
        try:
            filterDict["stars"] = float(minStar)
        except ValueError:
            print(Fore.RED + "you need to provide a number for minimum star filtering. Try search next time")
            print("*************************************************\n")
            return
        
    if city.lower() != "n/a" :
        num_not_n_a_filters += 1
        filterDict["city"] = city
    if name.lower() != "n/a" :
        num_not_n_a_filters += 1
        filterDict["name"] = name
    
    if (num_not_n_a_filters == 0):
        # all filterin were set to N/A so no searching ...
        print(Fore.RED + "All of the filtering items were set to N/A.. \n Please be more specific next time searching")
        print("*************************************************\n")
        return

    print("Order results by:\n"
          "type 1 to order by stars\n"
          "type 2 to order by city \n"
          "type 3 to order by name \n")
    order = int(input("order by: -> "))


    result = databaseRef.searchTable(filter=filterDict,tableName="business")
    print("*************************************************\n")
    if result:
        print(Fore.GREEN + "result is : \n ")
        if (order == 1):
            result = sorted(result, key=lambda x: x[5])
        elif (order == 2):
            result = sorted(result, key=lambda x: x[3])
        else:
            result = sorted(result, key=lambda x: x[1])

        index = 1
        for item in result:
            print(Fore.GREEN + f"{index}-")
            print(f"\n\t Business ID: {item[0]} \n\t Name: {item[1]}"
                f"\n\t Address: {item[2]} \n\t City: {item[3]} \n\t Rating(# of stars): {item[5]} \n")
            index += 1
    else:
        print(Fore.RED + "There are no business matching your filters.")

    print("*************************************************\n")


def searchUsers(databaseRef: DBServer):
    print("Please enters the filters,\n"
           "if you don't want to filter users by any of the following option, type N/A for that option")
    filterDict={}

    name = input("name of user: -> ")
    minStar = input("Minimum average stars: -> ")
    minCount = input("Minimum review counts: -> ")

    num_not_n_a_filters = 0
    if minStar.lower() != "n/a" :
        num_not_n_a_filters += 1
        try:
            filterDict["average_stars"] = float(minStar)
        except ValueError:
            print(Fore.RED + "you need to provide a number for Average star filtering. Try search next time")
            print("*************************************************\n")
            return
    
    if minCount.lower() != "n/a" :
        num_not_n_a_filters += 1
        try:
            filterDict["review_count"] = int(minCount)
        except ValueError:
            print(Fore.RED + "you need to provide a number for review count filtering. Try search next time")
            print("*************************************************\n")
            return

    if name.lower() != "n/a" :
        num_not_n_a_filters += 1
        filterDict["name"] = name


    if (num_not_n_a_filters == 0):
        # all filterin were set to N/A so no searching ...
        print(Fore.RED + "All of the filtering items were set to N/A.. \n Please be more specific next time searching")
        print("*************************************************\n")
        return
    
    result = databaseRef.searchTable(filter=filterDict,tableName="user_yelp")

    if result:
        # sorting the list of records by their name attributes
        result = sorted(result, key=lambda x: x[1])
        index = 1
        for item in result:
            print(Fore.GREEN + f"{index}-")
            print(f"\n\t User ID: {item[0]} \n\t Name: {item[1]}"
                f"\n\t Review Count: {item[2]} \n\t Useful: {item[4]} \n\t Funny: {item[5]}"
                f"\n\t Cool: {item[6]} \n\t Average Star: {item[8]} \n\t register date: {item[3]}")
            index += 1
    else:
        print(Fore.RED +"There are no users matching your filters.")

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