#Functionto add two numbers
def add_numbers(num1,num2):
    
    sum = num1 + num2
   
   # returning sum
    return sum

number1 = int(input("Enter number to add: "))
number2 = int(input("Enter another number to add: "))
# calling the function
print(add_numbers(number1,number2))
