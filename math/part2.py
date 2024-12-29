#gcd of two numbers using euclidean theorem
# gdc(a,b) = gcd(a%b,b) for all a>=b
a , b = 48, 18

while a!=0 and b!=0:
    if a>=b:
        a = a%b
    else:
        b =b%a
if a==0:
    print(b)
else:
    print(a)


# effective gcd using recursion
a, b=48, 18
def gcd(a, b):
    if a == 0:
        return b
    print(a,b)
    return gcd(b % a, a)
print(gcd(a,b))
