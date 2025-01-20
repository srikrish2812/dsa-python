"""
Left rotate the array by one place
"""
def left_rotate(arr=[1,2,3,4,5,6,7]):
    """
    TC = O(n)
    SC = O(1)
    """
    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i-1]=arr[i]
    arr[len(arr)-1] = temp
    return arr
print(left_rotate())


"""
Left rotate the array by k-places
"""
def kleft_rotate_brute(k=3,arr=[1,2,3,4,5,6,7]):
    """
    1. Store k-places in temp
    2. shift rest of the elements by k-places
    3. place the elements in temp at the end of array

    TC = O(n+k)
    SC = O(k)
    """
    temp = []
    n = len(arr)
    k = k%n
    for el in arr[0:k]:
        temp.append(el)

    for i in range(k,n):
        arr[i-k] = arr[i]

    for i in range(k):
        arr[n-k+i] = temp[i]

    print(f"After shifting {k} places arr = {arr}")

kleft_rotate_brute(k=10)


def kleft_rotate_optimal(k=3,arr=[1,2,3,4,5,6,7]):
    """
    1. Reverse the 1st k elements
    2. Reverse the last n-k elements
    3. Then reverse the whole array

    TC = O(k) + O(n-k) + O(n) = O(n)
    SC = O(1)
    We can also do this using slicing but this method
    does not have true O(1) space complexity
    arr = arr[k-1::-1] + arr[n-1:k_1:-1]
    arr = arr[::-1]
    """
    n = len(arr)
    k = k%n
    def reverse(arr,start,end):
        while start<end:
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1
    reverse(arr,0,k-1)
    reverse(arr,k,n-1)
    reverse(arr,0,n-1)
    print(arr)
kleft_rotate_optimal(k=6)

def linear_search(target=6, arr=[12,3,4,5,6,7,77]):
    """
    retunr the index of the target element in arr
    TC=O(n)
    SC = O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
print(linear_search())

def reverse(arr, start, end):
        while start<end:
            arr[start], arr[end] = arr[end], arr[start]
            start+=1
            end-=1



def rotateArray(nums=[1,2,3,4,5,6], x=2, y=1):
    """
    Rotate the array x times right andf y times left
    """
    #Write your code here...
    n = len(nums)
    #rotate right x places
    x=x%n
    reverse(nums, n-x,n-1)
    reverse(nums,0,n-x-1)
    reverse(nums,0,n-1)

    #rotate left y places
    y=y%n
    reverse(nums,0,y-1)
    reverse(nums,y,n-1)
    reverse(nums, 0,n-1)
    return nums
print(rotateArray())
