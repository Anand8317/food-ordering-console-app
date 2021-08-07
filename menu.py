from admin import createAdmin, adminLogin, addFood, editFood, viewFoodItems, delFood
from user import registerUser, login, newOrder, orderHistory, update
def menu():
    flag = True
    while (flag == True):
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        print("\n")
        
        choice = int(input("Enter your choice "))
        print("\n")
        
        if (choice == 1):
            flag1 = True
            while (flag1 == True):
                print("1. Register admin")
                print("2. Login admin")
                print("3. Go back")
                print("\n")
                choice1 = int(input("Enter your choice "))
                
                if (choice1 == 1):
                    createAdmin()
                if (choice1 == 2):
                    username = input("Enter your username ")
                    password = input("Enter your password ")
                    
                    flag2 = adminLogin(username, password)
                    if (flag2 == False):
                        break;
                        
                    flag3 = True
                    while (flag3 == True):
                        print("1. Add food item")
                        print("2. Edit food item")
                        print("3. View food item")
                        print("4. Delete food item")
                        print("5. Go back")
                        print("\n")
                        choice = int(input("Enter your choice "))
                        
                        if (choice == 1):
                            addFood()
                        if (choice == 2):
                            foodId = int(input("Enter food Id "))
                            editFood(foodId)
                        if (choice == 3):
                            viewFoodItems()
                        if (choice == 4):
                            foodId = int(input("Enter food Id "))
                            delFood(foodId)
                        if (choice == 5):
                            break
                if (choice1 == 3):
                    break
                    
        if (choice == 2):
            flag4 = True
            while (flag4 == True):
                print("1. Register")
                print("2. Login")
                print("3. Go back")
                print("\n")
                choice1 = int(input("Enter your choice "))
                
                if (choice1 == 1):
                    registerUser()
                if (choice1 == 2):
                    emailId = input("Enter your username ")
                    password = input("Enter your password ")
                    
                    flag5 = login(emailId, password)
                    if (flag5 == False):
                        break;
                        
                    flag6 = True
                    while (flag6 == True):
                        print("1. Place new order")
                        print("2. Order history")
                        print("3. Update profile")
                        print("4. Go back")
                        print("\n")
                        choice = int(input("Enter your choice "))
                        
                        if (choice == 1):
                            newOrder(emailId)
                        if (choice == 2):
                            orderHistory(emailId)
                        if (choice == 3):
                            emailId = update(emailId)
                        if (choice == 4):
                            break
                        
                if (choice1 == 3):
                    break
                    
        if (choice == 3):
            break