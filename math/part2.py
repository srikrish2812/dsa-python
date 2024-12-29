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
