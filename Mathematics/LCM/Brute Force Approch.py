# Find LCM of two number using simpler approach

def gcd(a, b):
    s = min(a, b)
    while s:
        if a % s == 0 and b % s == 0:
            break
        s = s - 1
    return s


def lcm(a, b):
    return (a / gcd(a, b)) * b


if __name__ == '__main__':
    a, b = map(int, input("Enter two values for A and B:- ").split())
    print("LCM of (%d,%d) is %d" % (a, b, lcm(a, b)))
