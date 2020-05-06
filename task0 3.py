number = int(input("Enter a number "))
count=0
while (number>0):
    number = number//10
    count = count + 1
print(f"Total no. of digits = {count}")