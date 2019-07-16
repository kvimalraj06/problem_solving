r=int(input("Enter upper limit: "))
l=[]
for a in range(2,r+1):
    k=0
    for i in range(2,a):
        if(a%i==0):
            k=k+1
    if(k<=0):
        l.append(str(a))
print(",".join(l))