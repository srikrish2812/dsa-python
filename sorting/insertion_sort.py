"""
Insertion Sort:
    1. Insert last element in the range in it's correct position
    2. Start the range with the second element in the array from left(i=1)
    3. Increase range by 1

In other words it takes the last element in each sub-array strating from left
and places it in the correct position and increases the sub-array range.

Worst case TC = O(n^2)
Average TC = O(n^2)
Best case TC = O(n) # when array is already sorted
"""

def insert_sort(arr):
    n = len(arr)
    for i in range(1,n):
        # this while loop makes sure that j always points to the
        # last element in the range in the array setting of the outer loop's iteration
        j=i
        while arr[j-1]>arr[j] and j>=1:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j-=1
    return arr

def main():
    arr = [70,60,50,40,30,20,10]
    print(insert_sort(arr=arr))

if __name__=="__main__":
    main()
