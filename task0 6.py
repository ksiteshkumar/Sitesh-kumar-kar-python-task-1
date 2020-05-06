n= int(input("Enter how many numbers you want in your series: "))
A=0
B=1
for i in range (n):
    print(A)
    Sum=A
    A=B
    B=Sum+B