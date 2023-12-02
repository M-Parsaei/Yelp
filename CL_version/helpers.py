from contorllers import searchTable

def searchBusiness():
    print("Please enters the filters,\n"
           "if you don't filter business by any of the following option, type N/A for that option")
    filteringList={}
    #filteringList["stars"]=input("Minimum number of business stars: -> ")
    #filteringList["city"]=input("city of business: -> ")
    filteringList["name"]=input("name of business: -> ")

    for key,value in filteringList.items():
        if value.lower()=="n/a":
            filteringList.pop(key)
    
    print("Order results by:\n"
          "type 1 to order by stars\n"
          "type 2 to order by city \n"
          "type 3 to order by name \n")
    order = input("order by: -> ")
    

    
    #result = searchTable(filter={"name":"kfc"},
    #                               tableName="business",
    #                               )

    #print(result)


    result = searchTable(filter=filteringList,tableName="business")
    print("result is : \n ")
    print(result)


def searchUsers():
    pass

def addFriend():
    pass

def addReview():
    pass