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
print(f"Number of digits in {n} = {count}")
#
