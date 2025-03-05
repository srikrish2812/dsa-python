"""
Print only 1 subsequence such that sum==k
"""

def print_subsequence(i,v,s,arr,n,k):
    if i>=n:
        if s==k:
            print(*v)
            return True
        return False

    v.append(arr[i])
    s+=arr[i]
    if print_subsequence(i+1, v,s,arr,n,k):
        return True

    v.pop()
    s-=arr[i]
    if print_subsequence(i+1, v,s,arr,n,k):
        return True

    return False

if __name__=="__main__":
   ARR = [4,9,5]
   K=9
   v=[]
   i=0
   s=0
   print_subsequence(i,v,s,ARR,len(ARR),K)
