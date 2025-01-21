"""
Union of two sorted arrays:
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


"""
You are given a sorted integer array and your task is to return
a new array that contains the squares of each element in arr,
sorted in non-decreasing order

input: [-5,-1,0,3,6]
output: [0,1,9,25,36]
"""

class solution:
    """
    TC = O(n)
    SC = O(n)

    1. The extremes will have the maximum absolute values.
    2. Keep two pointers at the start and end values
    3. Compare these extreme values and insert the maximum
    in the last position in the ans[] array and do it in a loop
    4. Reduce the range inwards
    """
    def getSortedSquares(self, arr):
        #Write your code here...
        n = len(arr)
        ans = [0]*n
        left=0
        right=n-1
        for i in range(n-1,-1,-1):
            if abs(arr[left])>abs(arr[right]):
                ans[i] = arr[left]**2
                left+=1
            else:
                ans[i] = arr[right]**2
                right-=1
        return ans
