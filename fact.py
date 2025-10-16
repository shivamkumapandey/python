def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Input from user
num = int(input("Enter a number: "))

print(f"The factorial of {num} is: {factorial(num)}")
