N = int(input("enter the value: "))
factorial = 1
for i in range(1, N+1):
    factorial = factorial * i
print("factorial of", N, "is", factorial)
