"""
Print all the subsequences with sum=k
"""
ARR = [4,9,5]
N=len(ARR)
K=9
def print_subseq_sumk(i,v,s,k=K,arr=ARR,n=N):
    """
    TC = O(2^n * n)
    SC = recursion stack space + auxillary space for variables = O(n)+O(n)=O(n)
    """
    if i>=n:
        if s==k:
            print(*v)
        return
    # picks
    v.append(arr[i])
    s+=arr[i]
    print_subseq_sumk(i+1,v,s,k,arr,n)

    # not pick
    v.pop()
    s-=arr[i]
    print_subseq_sumk(i+1,v,s,k,arr,n)

if __name__=="__main__":
    v=[]
    s=0
    i=0
    print_subseq_sumk(i,v,s)
