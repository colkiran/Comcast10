
def fact(num):
    while num!=1:
        return num * fact(num-1)
    return 1

print(fact(5))

print("-" * 40)

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n= int(input())
for i in range(n):
    print(fibo(i), end=" ")
print()

