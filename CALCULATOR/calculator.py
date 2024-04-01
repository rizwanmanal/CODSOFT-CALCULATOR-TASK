
num1=int(input("ENTER FIRST NUMBER:  "))

num2=int(input("ENTER SECOND NUMBER: "))

option=input("Enter '+' for addition,  '-' for subtraction,   '*' for multiplication ,     '/' for division :")

def  calculator():


    if option=='+':
        print(f"ADDITION OF TWO NUMBERS IS:{num1+num2}")
    elif option=='-':
        print(f"SUBTRACTION OF TWO NUMBERS IS:{num1-num2}")
    elif option=='*':
        print(f"MULTIPLICATION OF TWO NUMBERS IS:{num1*num2}")
    elif option=='/':
        print(f"DIVISION OF TWO NUMBERS IS:{num1/num2}")
    elif option=='%':
        print(f"MODULUS OF TWO NUMBERS IS:{num1%num2}")
    else:
        print("ERROR: Invalid Option")

# CALLING FUNCTION
calculator()





