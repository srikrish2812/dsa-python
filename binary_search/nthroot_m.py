"""

Find the nth root of an integer
"""

def brute_force(n,m):
    
    for i in range(m):
        if i**n==m:
            return i
    return -1

print(f"Using brute force: {brute_force(3,64)}")