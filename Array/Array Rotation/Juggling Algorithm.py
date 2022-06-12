#Juggling Algorithm for Array Rotation.

# To find GCD
def g_c_d(a,b):
    if(b == 0):
        return a
    return g_c_d(b,a%b)

arr = list(map(int,input().split())) #Array Input
n = len(arr)
d = int(input("Enter No. of Steps: "))
d = d % n  #If d is greater then n
gcd = g_c_d(n,d)  # To do partition.
for i in range(0,gcd):
    temp = arr[i]
    j = i
    while 1:
        k = j + d
        if k >= n:
            k = k - n
        if k == i:
            break
        arr[j] = arr[k]
        j = k
    arr[j] = temp
print("Array After the rotation: " , arr)