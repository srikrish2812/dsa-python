# print digits of a number in reverse order
n = 56789
print("-"*10 + f"Printing digits of {n} in reverse order" + "-"*10)
while n!=0:
    last_digit = n%10
    n = n//10
    print(last_digit)

print('--'*30)

# count the number of digits
n = 56789
num = n
count = 0
while num!=0:
    num = num//10
    count +=1
print(f"Number of digits in {n} = {count}\n")

# Reverse a number
num = n
reversed_num = 0
while num!=0:
    last_digit = num%10
    reversed_num = reversed_num*10 + last_digit
    num = num//10
print(f"Reverse of number {n} = {reversed_num}\n")

# check if num is palindrome or not
NUM = 1331
num = NUM
rev_num = 0
while num!=0:
    last_digit = num%10
    rev_num = rev_num*10 + last_digit
    num //=10
if NUM == rev_num:
    print(f"{NUM} is a Palindrome\n")
else:
    print(f"{NUM} Not a Palindrome\n")


# print all the divisors of a number

n = 36
divisors = []
# O(sqrt(n))
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        divisors.append(i)
        if i!=n//i:
            divisors.append(n//i)
divisors.sort() # O(sqrt(n))
print("-"*10 + f"Divisors of {n}" + "-"*10)
for i in divisors: # O(no of divisors)
    print(i)
print("--"*20)


# check if the prime or not

count = 0
for i in range(1, int(n**0.5)+1):
    if n%i==0:
        count+=1
        if i!=n//i:
            count+=1
if count ==2:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime, num of divisors = {count}")
