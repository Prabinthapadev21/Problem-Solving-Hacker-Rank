# Computing the sum of two integers.
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))

def returnsum(num1,num2):
    return num1+num2
 
result = returnsum(num1,num2)
print(f"The sum of the two numbers is {result}")