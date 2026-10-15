import cal as ca

USER_DATA = {
    "username":"admin",
    "acc.no" : 123456,
    "pin" :1234,
    "balance" : 1000000
}

def user_info():
   
   if USER_DATA and USER_DATA["username"]:
     return (f"\N Hi User {USER_DATA['username']} your account no is {USER_DATA['acc.no']}")

   else:
      print("User Not Found")

def deposit(deposit_amount):
   if deposit_amount:
        amount= ca.deposit_amount(USER_DATA['balance'], deposit_amount)
        USER_DATA['Balance'] = amount
        return amount 

def withdraw(withdraw_amount):
   
   if withdraw_amount:
      amount = ca.withdraw_calc(USER_DATA['balance'], withdraw_amount)
      USER_DATA['balance'] = amount
      return amount

def check_balance():
   return USER_DATA['Balance'] 

def main():
   print("Welcome to TP ATM...") 
   pin_no = int(input("Enter the Pin no :"))

   if USER_DATA and USER_DATA ["PIN"] == pin_no:

      print(user_info())

      while True:


        choice = int(input("""
        1.Deposit
        2.Withdraw
        3.Check Balance
        4.Exit
        Enter Your Choice : """)) 

        match choice:

           case 1:
              amount = int(input("Enter The Amount :"))
              print(f"Deposit Successfully!!,Your Total Balance is : {deposit(amount)}")
           case 2:
              amount = int(input("Enter the amount :"))
              print(f"Withdraw Successfully!!!,Your Total Balance is : {withdraw(amount)}")
           case 3:
              print(f"Your Balance Is:{check_balance()}")

           case 4:
              print("Thanks for Using TP ATM") 
              break
           case _:
              print("Invalid choice,Please select b/w 1 to 4") 

if __name__ == "__main__":
       main()

           

