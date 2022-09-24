# Count the number of digits in an integer using Log function
import math


def countdigit(num):
    return math.floor(math.log10(num)) + 1


if __name__ == '__main__':
    n = int(input("Enter the Number:- "))
    print("Number of Digits in %d = %d" % (n, countdigit(n)))
