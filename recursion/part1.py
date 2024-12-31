def cal_sum(n=10):
    if n==0:
        return 0
    else:
        return n+cal_sum(n-1)
print(cal_sum())
print(cal_sum(n=25))


def rec_gcd(a=48, b=54):
    if a==0:
        return b
    return rec_gcd(b%a,a)

print(rec_gcd())
