# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        if  choice == "1":
            print("check balane = : ", balance,)
        if  choice == "2":
            print("check : ", balance ,)
            Withdraw = float(input("Enter withdraw : "))
            if Withdraw > 1000:
                print("not money")
            if Withdraw <= 1000:
                print("Completed successfully")
            if Withdraw < 0:
                print("cannot depsosit less than 0")
            else:    
                balance=balance - Withdraw
                print("please collect your money, and your balance now = ", balance)            
        if  choice == "3":
            Deposit= float(input("Enter Deposit : "))
            if Deposit < 0:
                print("cannot depsosit less than 0")
            else:
              balance=balance + Deposit
              print("Your balance now =",balance)      
        if  choice == "4":
            break
        else:
            print("Exit")
            continue
else:
    print("Invalid PIN")