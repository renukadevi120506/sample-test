no1 = float(input("Enter the 1st number:"))
opr = input("Enter the Operator(+,-,*,/):")
no2 = float(input("Enter the 2nd Number:"))

if opr=="+":
    result = no1 + no2

elif opr=="-":
    result = no1 - no2

elif opr=="*":
    result =no1 * no2

elif opr =="/":
    if no2 !=0:
     result = no1 / no2
    else:
      result=("Zero is invalid")
else:
   print("Invalid Inputs,Please valid inputs only!!")  

print(f"Result:{result}")                
    

