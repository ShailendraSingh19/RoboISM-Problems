def number_fact(a):
    n = 0
    for i in range(1,a+1):
        if ((a%i) == 0):
            n += 1
    return(n)
def primes(a,b):
    t = []
    for i in range(a,b+1):
        if (number_fact(i)==2):
            t.append(i)
    return(t)
#a = int(input())
#b = int(input())
print(primes(23,89))