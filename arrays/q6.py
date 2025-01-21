"""
Union of two arrays:
"""

def brute_force(a=[3,3,4,5,6,10,7,7],b=[4,5,10,6,7,8,8]):
    """
    m -> len(a)
    n -> len(b)
    1. For one insertion in set it takes logx where x is
    number of elements in the combined set. In the worst case
    x = m+n
    2. For adding elements to set it takes (m+n)*logx
    3. Appending to list is single step operation
    TC = O(m+n*log(m+n))
    SC = O(2(m+n)) = O(m+n)
    """
    c = set()
    ans = []
    for el in a:
        c.add(el)
    for el in b:
        c.add(el)
    for el in c:
        ans.append(el)
    return ans

print("Brute Force Approach",brute_force())


def optimal(a = [3,3,4,5,6,7,7,10], b=[4,5,6,7,8,8]):
    """
    Optimal solution can be obtained using two pointer approach.
    For this to work the arrays a and b must be sorted
    TC = O(m+n)
    SC = O(m+n)
    """
    ans = []

    i,j=0,0
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            if not ans or a[i]!=ans[-1]:
                ans.append(a[i])
            i+=1
        else:
            if not ans or b[j]!=ans[-1]:
                ans.append(b[j])
            j+=1
    while j<len(b):
        if not ans or b[j]!=ans[-1]:
            ans.append(b[j])
        j+=1
    while i<len(a):
        if not ans or a[i]!=ans[-1]:
            ans.append(a[i])
        i+=1

    return ans

print("Optimal approach", optimal())
