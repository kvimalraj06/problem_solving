lis = []
dec = int(input("enter the decimal value: "))
temp = dec
bin = 0
while dec >= 1:
    bin = dec % 2
    lis.append(int(bin))
    dec = dec/2
lis.reverse()
print("the binary value of", temp, "is: ")
print("".join(str(i) for i in lis))