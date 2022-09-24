# Count the number of digits in an integer using Iteration

def countdigit(num):
    count = 0
    while num != 0:
        num = num // 10
        count = count + 1
    return count


if __name__ == '__main__':
    n = int(input("Enter the Number:- "))
    print("Number of Digits in %d = %d" % (n, countdigit(n)))
