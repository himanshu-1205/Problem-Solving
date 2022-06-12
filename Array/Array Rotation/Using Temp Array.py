#Array Rotation using Temporary Array.

arr = list(map(int,input().split())) #Array Input
n = len(arr)
d = int(input("Enter No. of Steps: "))
d = d % n  #If d is greater then n
temp = []
temp = arr[d:] + arr[:d]
print("Array After the rotation: " , temp)