from itertools import product
def primfac(val):#function to find the prime factors of numbers in array
    lis = []
    for i in range(2, val + 1):
        k = 0
        for j in range(2, i):
            if (i % j == 0):
                k = k + 1
        if (k <= 0 and val%i==0):
            lis.append(i)
    return (sum(lis))
def subset(k,n,arr):
    prime_sum = 0
    for i in arr:
        prime_sum += primfac(i)
    lis1=[]
    for i in range(prime_sum +1):
        lis1.append(i)
    lis1=list(product(lis1,repeat=k))
    count=0
    for i in lis1:
        if(sum(i)==prime_sum):
            count += 1
    print(count)
if __name__ == '__main__':
    k = 3# subset value
    n = 3# length of array
    arr = [1, 2, 6] #array
    subset(k, n, arr)


