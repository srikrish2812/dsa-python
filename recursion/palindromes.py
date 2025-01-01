"""
checking palindromes using recursion
"""
# without recursion time complexity O(n/2) = O(n)
def norec_pal(s):
    n = len(s)
    for i in range(0,n//2):
        if s[i]!=s[n-i-1]:
            return False
    return True

print(norec_pal(s="LEVELS"))


# with recursion
def rec_pal(i=0,s="LEVEL"):
    n = len(s)
    if i>=n//2: return True
    if s[i]!=s[n-i-1]:return False
    return rec_pal(i+1,s)

print(rec_pal(i=0, s="RADAR"))
