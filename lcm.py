num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
big = 0
lcm = 0
if num1 > num2:
    big = num1
else:
    big = num2
while(True):
    if(big % num1==0 and big%num2 ==0):
        lcm = big
        break
    else:
        big += 1
print("lcm of two numbers is ", lcm)
