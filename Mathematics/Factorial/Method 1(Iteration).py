# Find Factorial of a Number using Iteration

def factorial(num):
    fact = 1
    for i in range(2, num + 1):
        fact = fact * i
    return fact


if __name__ == '__main__':
    n = int(input("Enter the Number:- "))
    print("Factorial of %d = %d" % (n, factorial(n)))
