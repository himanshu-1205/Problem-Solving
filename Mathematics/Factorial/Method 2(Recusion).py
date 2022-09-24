# Find Factorial of a Number using Recursion

def factorial(num):
    if num == 1 or num == 0:
        return 1
    return num * factorial(num-1)


if __name__ == '__main__':
    n = int(input("Enter the Number:- "))
    print("Factorial of %d = %d" % (n, factorial(n)))
