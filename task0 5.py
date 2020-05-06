lower = int(input("Define the lower limit of the interval "))
upper = int(input("Define the upper limit of the interval "))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

check=int(input('Enter the number you want to check: '))
if check > 1 :
   for i in range(2,check):
    if (check%i)== 0:
        print(check,'is a prime number')
        break
    else:
        print(check,'is not a prime number')
    break
else:
    print(check,'is not a prime number')

