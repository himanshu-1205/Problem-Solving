# Count the number of digits in an integer using recursion

def countdigit(num):
    if num == 0:
        return 0
    return 1 + countdigit(num//10)


if __name__ == '__main__':
    n = int(input("Enter the Number:- "))
    print("Number of Digits in %d = %d" % (n, countdigit(n)))
