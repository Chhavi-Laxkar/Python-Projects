# Step 1. Create a function
def addition(num1 , num2):
    return num1 + num2  
def subtraction(num1 , num2):
    return num1 - num2      
def multiplication(num1 , num2):
    return num1 * num2  
def division(num1 , num2):
    return num1 / num2  
def modulus(num1 , num2):
    return num1 % num2  
def square_root(num1):
    return num1 ** 0.5  
def floor_division(num1 , num2):
    return num1 // num2
def percentage(num1 , num2):
    return (num1 / num2) * 100
def average(num1 , num2):
    return (num1 + num2) / 2

# Step 2. Select the operation
print("Please Select One Operation:\n"
       "1. Addition :\n"
       "2. Subtraction :\n"
       "3. Multiplication :\n"
       "4. Division :\n"
       "5. Modulus :\n"
       " 6. Square Root :\n"
       "7. Floor Division :\n"
       "8. Percentage :\n"
       "9. Average :\n")

select = int(input("Select operations from 1, 2, 3, 4, 5, 6, 7, 8, 9 :"))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Step 3. Print the result
if select == 1:
    print(num1, "+", num2, "=", addition(num1 , num2))
elif select == 2:       
    print(num1, "-", num2, "=", subtraction(num1 , num2))
elif select == 3:   
    print(num1, "*", num2, "=", multiplication(num1 , num2))
elif select == 4:   
    print(num1, "/", num2, "=", division(num1 , num2))
elif select == 5:
    print(num1, "%", num2, "=", modulus(num1 , num2))
elif select == 6:
    print("Square root of", num1, "=", square_root(num1))
elif select == 7:
    print(num1, "//", num2, "=", floor_division(num1 , num2))
elif select == 8:
    print(num1, "is", percentage(num1 , num2), "% of", num2)
elif select == 9:
    print("Average of", num1, "and", num2, "=", average(num1 , num2))
else :
    print("Invalid input.")
