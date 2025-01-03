"""
Selection sorting:
    1. Select the minimum
    2. Swap it with the first element in the current range
    3. Reduce the range/move the range to the right
"""
def sel_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index]>arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def main():
    arr=[70,40,30,10,50,20,60]
    print(sel_sort(arr=arr))

if __name__ == "__main__":
    main()
