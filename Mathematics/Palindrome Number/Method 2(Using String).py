# Check the number is palindrome or not using string reverse

def palindrome(num):
    num = str(num)
    revnum = num[::-1]
    return True if num == revnum else False


if __name__ == '__main__':
    n = int(input("Enter the Number:- "))
    if palindrome(n):
        print("Entered Number \"%d\" is Palindrome" % n)
    else:
        print("Entered Number \"%d\" is not Palindrome" % n)
