# Check the number is palindrome or not using string and compare half of the string

def palindrome(num):
    num = str(num)
    length = len(num)
    for i in range(0, length // 2):
        if num[i] != num[length - i - 1]:
            return False
    return True


if __name__ == '__main__':
    n = int(input("Enter the Number:- "))
    if palindrome(n):
        print("Entered Number \"%d\" is Palindrome" % n)
    else:
        print("Entered Number \"%d\" is not Palindrome" % n)
