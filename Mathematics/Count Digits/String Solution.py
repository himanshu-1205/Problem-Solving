# Count the number of digits in an integer using String conversion and then find length of the string.

def countdigit(num):
    return len(str(num))


if __name__ == '__main__':
    n = int(input("Enter the Number:- "))
    print("Number of Digits in %d = %d" % (n, countdigit(n)))
