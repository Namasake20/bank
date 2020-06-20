def bank():
    import getpass
    import datetime
    x = datetime.datetime.now()
    print(x)
    print(x.strftime("%B"))
    for i in range(0,3):
        print("""
        \t\t== welcome to barclays bank kenya==""" )
    
    pinCode = [4565 ,8775 , 1253, 9675]
    accountHoldersname = ["john caesar","emily bright","bright gameli","kissinja masake"]
    accountNumber = ["756453","647391","763212","076532"]
    balance = [7564535,867432,2453425,1342435]

    flag = False
    inputName = input("Enter your name: ")
    inputName = inputName.lower()
    inputPin = 0000
    index = 0

    for i,name in enumerate(accountHoldersname):
        count = 0
        if name == inputName:
         index = i
         inputPin = int(getpass.getpass("Enter your pin: "))

    if inputPin == pinCode[index]:
        flag = True
    else:
        print("Invalid data.")
        flag = False
    
    if flag == True:
        print("Your account number is: ",accountNumber[index])
        print("Your balance is : ",balance[index])
        withdrawordeposit = input("Do you want to withdraw or deposit: ")
        if withdrawordeposit == "withdraw":
            amount = input("Enter the amount you would like to withdraw: ")
            try:
                amount = int(amount)
                if amount > balance[index]:
                 raise
            except:
                print("Invalid input")
            remainingbalance = balance[index] - amount
            balance.remove(balance[index])
            balance.insert(index,remainingbalance)
            remainingbalance = print("Your remaining balance is: ",remainingbalance)
        elif withdrawordeposit == "deposit":
            amount = input("Enter the amount you would like to deposit: ")
            try:
                amount = int(amount)
                if amount > balance[index]:
                 raise
            except:
                print("Invalid input")
            remainingbalance = balance[index] + amount
            balance.remove(balance[index])
            balance.insert(index,remainingbalance)
            remainingbalance =print("Your remaining balance is: ",remainingbalance) 
        print("**Thank you our dear customer***")
            
            
bank()