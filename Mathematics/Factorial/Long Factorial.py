# Long Factorial. Basically for Number > 10


def multiply(num, arr_inc, big_array):
    carry = 0
    for i in range(0, arr_inc + 1):
        multi = (big_array[i] * num) + carry
        val = multi % 10
        big_array[i] = val
        carry = multi // 10
    while carry != 0:
        arr_inc = arr_inc + 1
        big_array[arr_inc] = carry % 10
        carry = carry // 10
    return arr_inc


def factorial(num):
    big_array = [None] * 500
    big_array[0] = 1
    arr_inc = 0
    for i in range(2, num + 1):
        arr_inc = multiply(i, arr_inc, big_array)
    print("Factorial of %d = " % num, end='')
    for i in range(arr_inc, -1, -1):
        print(big_array[i], end='')


if __name__ == '__main__':
    n = int(input("Enter the Number:- "))
    if n == 1 or n == 0:
        print("Factorial of %d = %d" % (n, 1))
    else:
        factorial(n)
