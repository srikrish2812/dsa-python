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
def kleft_rotate(k=3,arr=[1,2,3,4,5,6,7]):
    """
    1. Store k-places in temp
    2. shift rest of the elements by k-places
    3. place the elements in temp at the end of array
    """
    temp = []
    n = len(arr)
    for el in arr[0:k]:
        temp.append(el)

    for i in range(k,n):
        arr[i-k] = arr[i]

    for i in range(k):
        arr[n-k+i] = temp[i]

    print(f"After shifting {k} places arr = {arr}")

kleft_rotate()
