# Find GCD or HCF of two number using Euclidean Algorithm

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    a, b = map(int, input("Enter two values for A and B:- ").split())
    print("HCF of (%d,%d) is %d" % (a, b, gcd(a, b)))
