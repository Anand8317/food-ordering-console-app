from admin import food, viewFoodItems
user = dict()
def registerUser():
    newUser = dict()
    name = input("Enter your full name: ")
    contactNo = int(input("Enter contact No: "))
    emailId = input("Enter email Id: ")
    address = input("Enter your address: ")
    password = input("Enter password: ")
    print("\n")
    if emailId in user:
        print("\nAccount already exist\n")
        return
    newUser[emailId] = [name, contactNo, emailId, address, password, []]
    user.update(newUser)
    
def login(emailId, password):
    if emailId not in user:
        print("\n")
        print("Account doesn't exist")
        print("\n")
        return False

    if user[emailId][4] == password:
        print("\n")
        print("Successful login")
        print("\n")
        return True
    else:
        print("\n")
        print("Wrong password")
        print("\n")
        return False
    
def update(emailId):
    if emailId not in user:
        print("\n")
        print("Account doesn't exist")
        print("\n")
        return 
    
    newUser = dict()
    name = input("Enter your full name: ")
    contactNo = int(input("Enter contact No: "))
    newEmailId = input("Enter email Id: ")
    address = input("Enter your address: ")
    password = input("Enter password: ")
    print("\n")

    newUser[newEmailId] = [name, contactNo, emailId, address, password, []]
    for i in user[emailId][5]:
        newUser[newEmailId][5].append(i)
    user.update(newUser)
    del user[emailId]
    print("\n")
    return newEmailId

def newOrder(emailId):
    viewFoodItems()
    choice = input("\nSelect items from the list\n")
    List = list(choice)
    choiceList = []
    for item in List:
        try:
            choiceList.append(int(item))
        except:
            print("")
    print("\nYou have selected these items:\n")
    f = list(food.items())
    for i in choiceList:
        l = list(f[i-1][1])
        print(str(i) + ". " + l[0] + " (" + l[1] + ") [INR " + str(l[2]) + "]" )
        
    confirm = input("Place order (Y or N) ")
    if (confirm == "Y" or confirm == "y"):
        for i in choiceList:
            if food[f[i-1][0]][4] == 0:
                print("\nSome items are out of stock\n")
                print("\nOrder could not be placed\n")
                return
        for i in choiceList:
            food[f[i-1][0]][4] -= 1
            l = list(f[i-1][1])
            item = l[0] + " (" + l[1] + ") [INR " + str(l[2]) + "]"
            user[emailId][5].append(item)
            
        print("\nYour order is placed\n")
            
    else:
        print("\nYour order is not placed\n")

def orderHistory(emailId):
    print("\n")
    print("your order history")
    for i in user[emailId][5]:
        print(i)
    print("\n")
