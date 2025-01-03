"""
Insertion Sort:
    1. Insert last element in the range in it's correct position
    2. Start with range 2 from left
    3. Increase range by 1

Worst case TC = O(n^2)
Average TC = O(n^2)
Best case TC = O(n)
"""

def insert_sort(arr):
    n = len(arr)
    for i in range(1,n):
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
