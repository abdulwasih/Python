#Armstrong number
#import math
number = int(input("Enter the number : "))

temp = number

sum=0
while temp > 0:
    k = temp%10
    sum = sum+(k**3)
    #print(sum)
    temp = temp//10
    #print(temp)
if sum == number:
    print("The given number is armstrong")
else:
    print("The given number is not armstrong")
   
 
