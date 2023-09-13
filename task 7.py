num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

def add_without_plus(num1, num2):
    while num2 != 0:
        carry = num1 & num2
        num1 = num1 ^ num2
        num2 = carry << 1
    return num1
result = add_without_plus(num1, num2)
print("The sum is:", result)