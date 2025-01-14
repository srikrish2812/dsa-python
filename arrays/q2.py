"""
Find the second largest element
"""
# Brute force approach 1:
# sort first and then find the second largest
def appr_1(arr):
    # TC = O(nlogn) + O(n) [sorting+looping]
    # SC = O(n) [sorting additional space]
    n = len(arr)
    arr.sort()
    i = n-2
    while i>=0:
        if arr[i]!=arr[n-1]:
            return arr[i]
        i-=1
    return None

arr = [7,7,8,8,8,5,6]
print("Brute Force 1:", appr_1(arr))

# Approach 2:
# Find max element first and then find second largest element
def appr_2(arr):
    #n = len(arr)
    # TC = O(2N) [2 loops till we find a solution]
    # SC = O(1)
    max_el = arr[0]
    for el in arr:
        if el>max_el:
            max_el = el

    sec_el = float('-inf')
    for el in arr:
        if el>sec_el and el!=max_el:
            sec_el = el
    return sec_el

print("Approach 2:", appr_2(arr))

# Optimal Approach - Appraoch 3:
def appr_3(arr):
    # TC = O(n)
    # SC = O(1)
    max_el = arr[0]
    sec_lar = float('inf')
    for el in arr:
        if el>max_el:
            sec_lar = max_el
            max_el = el
        elif max_el>el and el>sec_lar:
            sec_lar = el
    return sec_lar
arr = [50,40,20,10,60]
print("Optimal approach:", appr_3(arr))
