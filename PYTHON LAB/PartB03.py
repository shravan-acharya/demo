def divide_number():
    try:
        num1=int(input("Enter the numerator:"))
        num2=int(input("Enter the denominator:"))
        num3=num1/num2
        print(num3)
    except ValueError:
        print("Please enter a numeric value")
    except ZeroDivisionError:
        print("Please enter a non-zero value")
    finally:
        print("Exception complete")
divide_number()
