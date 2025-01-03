def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))


# sum of primes till nth fibonacci
fib_cache = {}
def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def get_fib(n):
    if n in fib_cache:
        return fib_cache[n]
    if n<=1:
        return n
    fib_cache[n] = get_fib(n-1) + get_fib(n-2)
    return fib_cache[n]

def sum_nthfib(n):

    s = 0
    for i in range(n+1):
        ith_fib = get_fib(i)
        if is_prime(ith_fib):
            s+=ith_fib
    return s

#print(sum_nthfib(52))
