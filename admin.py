admin = {"admin":"admin"}
food = dict()

def createAdmin():
    newAdmin = dict()
    username = input("Enter username ")
    password = input("Enter password ")
    newAdmin[username] = password
    if username in admin:
        print("\nAdmin already exist\n")
    else:
        admin.update(newAdmin)
        print("\nNew Admin has been created\n")
    
def adminLogin(username, password):
    if not username in admin:
        print("Account doesn't exist")
        print("\n")
        return False
    if admin[username] == password:
        print("\n")
        print("Successful login")
        print("\n")
        return True
    else:
        print("\n")
        print("Wrong password")
        print("\n")
        return False

def addFood():
    newFood = dict()
    foodId = id(newFood)
    newFood[foodId] = ["","",0,0,0]
    newFood[foodId][0] = input("Enter food name: ")
    newFood[foodId][1] = input("Enter food quantity: ")
    newFood[foodId][2] = int(input("Enter food price: "))
    newFood[foodId][3] = int(input("Enter food discount: "))
    newFood[foodId][4] = int(input("Enter the stock: "))
    food.update(newFood)
    print("\nFood item has been added")
    print("\nFood item Id is ",foodId)
    print("\n")
    
def editFood(foodId):
    if foodId not in food:
        print("\nFood id not found\n")
        return
    food[foodId][0] = input("Enter food name: ")
    food[foodId][1] = input("Enter food quantity: ")
    food[foodId][2] = int(input("Enter food price: "))
    food[foodId][3] = int(input("Enter food discount: "))
    food[foodId][4] = int(input("Enter the stock: "))
    print("\n Food item has been edited\n")

    
def viewFoodItems():
    i = 1
    for foodId in food:
        print("\n")
        print(str(i) + ". " + food[foodId][0] + " (" + food[foodId][1] + ") [INR " + str(food[foodId][2]) + "]" )
        i += 1
    print("\n")
    
def delFood(foodId):
    if foodId not in food:
        print("\nFood id not found\n")
        return
    del food[foodId]
    print("\nFood Item has been deleted\n")