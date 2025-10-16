def is_prime(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    # Check factors from 2 to the square root of num
    for i in range(2, int(num**0.5) + 1):  
        if num % i == 0:
            return False  # num is divisible by i, so it's not prime
    return True  # No factors found, num is prime

# Input from user
number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
