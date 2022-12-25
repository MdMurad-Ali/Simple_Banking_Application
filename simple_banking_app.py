username = "X"
password = "123456"
balance = 0
def ShowBalance():
    print("Your account balance is "+str(balance))
    
def Check(us,p):
    return (username==us and p==password)
    
def AddMoney():
    print("Enter amount to add : ", end=" ")
    amn = int(input())
    global balance
    balance+=amn
    ShowBalance()
    
def DepositMoney():
      global balance
      print("Enter amount to deposit : ", end=" ")
      amn= int(input())
      if(amn > balance): print("No sufficient balance to deposit.")
      else :
         balance-=amn
         ShowBalance()
    
while(True):
    print("Enter username : ", end=" ")
    user = input()
    print("Enter password : ", end=" ")
    pw = input()
    c = Check(user,pw)
    if(c==False): print("Invalid password or username!")
    while(c): 
        print("\nX - Dashboard : ")
        balance  = 0
        while(True):
           print("\nEnter\n1 to Add Money\n2 to Deposit Money\n3 to Show\n4 to Exit\n")
           inp = int(input())
           if(inp==1): AddMoney()
           elif (inp==2): DepositMoney()
           elif(inp==3):  ShowBalance()
           elif(inp==4): break
           else : print("Invalid Input!")
        break
    print("\nEnter\n1 to Continue\n2 to Exit\n")
    q = int(input())
    if(q==2): break
    elif(q!=1): print("Invalid Input!\n")