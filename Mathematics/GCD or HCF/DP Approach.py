# function to return gcd of a and b

# Taking the matrix as globally
dp = [[-1 for i in range(1001)] for j in range(1001)]


def gcd(a, b):
    # Everything divides 0
    if a == 0:
        return b
    if b == 0:
        return a

    # base case
    if a == b:
        return a

    if dp[a][b] != -1:
        return dp[a][b]

    # a is greater
    if a > b:
        dp[a][b] = gcd(a - b, b)
    else:
        dp[a][b] = gcd(a, b - a)

    return dp[a][b]


# Driver program to test above function
a, b = map(int, input("Enter two values for A and B:- ").split())
if gcd(a, b):
    print('GCD of (',a,',',b,')is:- ', gcd(a, b))
else:
    print('not found')
