# Find GCD or HCF of two number using simpler approach

def gcd(a, b):
    s = min(a, b)
    while s:
        if a % s == 0 and b % s == 0:
            break
        s = s - 1
    return s


if __name__ == '__main__':
    a, b = map(int, input("Enter two values for A and B:- ").split())
    print("HCF of (%d,%d) is %d" % (a, b, gcd(a, b)))
