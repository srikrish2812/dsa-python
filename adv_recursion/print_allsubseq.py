"""
Print all the subsequences of an array:

"""
ARR = [4,5,6]
N = len(ARR)
def print_subseq(i:int,v:list,arr:list=ARR,n:int=N):
    if i>=n:
        print(*v)
        return

    # picks current element
    v.append(arr[i])
    print_subseq(i+1,v,arr,n)

    # doesn't pick current element
    v.pop()
    print_subseq(i+1,v,arr,n)

if __name__ == "__main__":
    v=[]
    print_subseq(0,v,ARR,N)
