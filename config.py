num_factorial = int(input('num: '))
def factorial(n):
    p=1
    for i in range(2,n+1):
        p=p*i
    print(p)
factorial(num_factorial)