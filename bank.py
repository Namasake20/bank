def kcb():
   import datetime
   import getpass
   pinCode = ["4078", "5647", "0342", "4782", "7604"]
   Accountholdersname = ["masake caleb","samantha Dawson","raymond reddington","tom hanks","frank underwood"]
   AccountNumber = [464754, 7548975, 563863, 763786, 7589730]
   Accountbalance = [34500, 300450, 670433, 9070403, 263536235]

   x = datetime.datetime.now()
   print(x)
   
   for i in range (3):
    print("""
 \t\t=== Welcome to kcb bank=== """)
    inputName = input("Enter your name: ")
    inputName = inputName.lower()
    inputPin = 0000
    index = 0
    flag = False
    for i,name in enumerate(Accountholdersname):
      if name == inputName:
        inputPin = getpass.getpass("Enter your pin: ")
        print(i)
        index=i
    if inputPin == pinCode[index]:
        flag = True
    else:
        print("Invalid data")
        flag = False
        continue
    if flag == True:
        print("Your account number is: ",AccountNumber[index])
        print("Your balance is: ",Accountbalance[index])
        WithdrawOrDeposit = input("Do you want to withdraw or Deposit cash?: ")
        if WithdrawOrDeposit == "withdraw":
          amount = input("Enter the amount your would like to withdraw: ")
          try:
             amount = int(amount)
             
          except:
             print("Invalid input")
         
        remainingbalance = Accountbalance[index]- amount
        Accountbalance.remove(Accountbalance[index])
        Accountbalance.insert(index,remainingbalance)
        availablebalance = print("Your available is: ",remainingbalance)
kcb()


         
