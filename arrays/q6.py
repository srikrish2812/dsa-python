"""
Union of two arrays:
"""

def brute_force(a=[3,3,4,5,6,10,7,7],b=[4,5,6,7,8,8]):
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

print(brute_force())
