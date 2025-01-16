"""
1. Check if array is sorted
2. Remove duplicates:
    a. Two pointer method is optimal approach
"""
def is_sorted(arr):
    # TC = O(n)
    # SC = O(1)
    n = len(arr)
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            return False
    return True

arr_1 = [2,3,3,4,5,11]
arr_2 = [2,3,4,10,5,12]
print(f"Check if {arr_1} is sorted: {is_sorted(arr_1)}")
print(f"Check if {arr_2} is sorted: {is_sorted(arr_2)}")

#brute force approach
def rem_dup(arr):
    #TC = O(nlogn+n)
    #SC = O(n)
    s = set()
    for i in range(len(arr)):
        s.add(arr[i])
    j = 0
    for k in s:
        arr[j] = k
        j+=1
    return len(s)
a = [5,5,7,7,9,9]
print(rem_dup(a))
print(a)

# Remove duplicates Optimal Approach
# This is called two pointer method
def opt_remdup(arr):
    #TC = O(n) [for loop]
    #SC = O(1)
    i = 0
    j = 1
    for j in range(1,len(arr)-1):
        if arr[i]!=arr[j]:
            arr[i+1] = arr[j]
            i+=1
    return i+1 # returns the num of unique elements

arr = [5,5,7,7,9,9]
print(opt_remdup(arr),'\n',arr)
