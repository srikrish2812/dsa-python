"""
Print only 1 subsequence such that sum==k
"""

def print_subsequence(i,v,s,arr,n,k, is_printed):
    """
    Using a mutable object for is_printed:
    Instead of passing a boolean (is_printed), we pass a list [False].
    Lists are mutable, so changes to is_printed[0] in one recursive
    call are reflected in all other calls.This ensures that once a valid
    subsequence is printed, no further subsequences are printed.

    Stopping further recursion:

    After printing a valid subsequence, we set is_printed[0] = True.
    This prevents the function from printing any other subsequences.
    """
    if i>=n:
        if s==k and is_printed[0]==False:
            print(*v)
            is_printed[0]=True
        return

    v.append(arr[i])
    s+=arr[i]
    print_subsequence(i+1, v,s,arr,n,k,is_printed)

    v.pop()
    s-=arr[i]
    print_subsequence(i+1, v,s,arr,n,k,is_printed)


def alt_implementation(i,v,s,arr,n,k):
    # base case
    if i>=n:
        if s==k:
            print(*v)
            return True
        return False

    # pick
    v.append(arr[i])
    s+=arr[i]
    if alt_implementation(i+1,v,s,arr,n,k): return True

    # not pick
    v.pop()
    s-=arr[i]
    if alt_implementation(i+1,v,s,arr,n,k): return True

    return False

if __name__=="__main__":
   ARR = [3,4,7]
   K=7
   v=[]
   i=0
   s=0
   print_subsequence(i,v,s,ARR,len(ARR),K,[False])
   alt_implementation(i,v,s,ARR,len(ARR),K)
