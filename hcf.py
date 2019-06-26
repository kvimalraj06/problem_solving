num1 = int(input("enter the frst number: "))
num2 = int(input("enter the second number: "))
smaller = 0
hcf = 0
if(num1 > num2):
    smaller = num2
else:
    smaller = num1
for i in range(1, smaller + 1):
    if(num1 % i == 0 and num2 % i == 0):
        hcf = i
print("HCF of the numbers is",hcf)

