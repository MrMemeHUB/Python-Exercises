primeInput = int(input("Type a number and I'll tell you if it's a prime number or not:"))

def checkPrime(number):
    if primeInput % 2 == 0:
        print("It's not a prime number!")
    elif primeInput % 3 == 0:
        print("It's not a prime number!")
    else:
        print("It's a prime number!")

checkPrime(primeInput)
