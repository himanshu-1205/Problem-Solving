# Check the number is palindrome or not.

def palindrome(num):
    rnum = 0
    while num != 0:
        rem = num % 10
        rnum = (rnum * 10) + rem
        num = num // 10
    return rnum


if __name__ == '__main__':
    n = int(input("Enter the Number:- "))
    if n == palindrome(n):
        print("Entered Number \"%d\" is Palindrome" % n)
    else:
        print("Entered Number \"%d\" is not Palindrome" % n)
