def add(x,y):
    return x+y
def subtract(x,y):
    return x-y

#this function multiplies two numbers
def multiply(x,y):
    return x*y

#this fuction divides two numbers
def divide(x,y):
    return x/y


print("select operation.")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    #take input from the user
    choice=input("enter choice(1/2/3/4):")

    #check if choice is one of the four options
    if choice in ('1','2','3','4'):
        try:
            num1=float(input("enter first number:"))
            num2=float(input("enter second number:"))
        except valueError:
            print("invalid input.please enter the number.")
            continue

        if choice=='1':
            print(num1,"+",num2,"=",add(num1,num2))

        elif choice=='2':
            print(num1,"-",num2,"=",subtract(num1,num2))

        elif choice=='3':
            print(num1,"*",num2,"=",multiply(num1,num2))

        elif choice=='4':
            print(num1,"/",num2,"=",divide(num1,num2))


        #check if user wants another calculation
        #break the while loop if answer is no
        next_calculation=input("lets do next calculation?(yes/no):")
        if next_calculation=="no":
            break
        elif next_calculation=="yes":
            continue
    else:
        print("invalid input")
             
                  
                

    
