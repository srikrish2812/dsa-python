"""
Quick Sort:
    1. Select a pivot. Pivot is the first element in the range
    2. Place pivot in the correct position in the sorted array
    3. Create a parition at the pivot by placing elements less
    than pivot to the left and place elements greater than pivot
    to the right

Worst Case TC = O(n^2) (array is already sorted)
Best Case TC = O(nlogn) (partition happens at the middle)

Worst case additional Space complexity = O(1)

Best case Stack space complexity = O(logn) (happens when paritition happens at the middle)
Worst case Stack space complexity = O(n) (array is already sorted)
"""
def partition(arr, low, high):
    i = low
    j = high
    while i<j:
        while arr[i]<=arr[low] and i<=high-1: # increment i
            i+=1
        while arr[j]>arr[low] and j>=1: # decrement j
            j-=1
        if i<j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j

def quick_sort(arr, low, high):
    if low<high:
        # at index j partition occurs
        j = partition(arr, low, high) # return the index j
        quick_sort(arr,low,j-1)
        quick_sort(arr,j+1, high)
    else:
        return

def main():
    arr = [11,17,9,13,16,7,4,10,6]
    high = len(arr)-1
    quick_sort(arr=arr,low=0,high=high)
    print(' '.join(list(map(str,arr))))



if __name__ =="__main__":
    main()
