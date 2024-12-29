class solution:
    def gcd(self, N, arr):
        #Code here
        def get_hcf(a,b):
            while a!=0 and b!=0:
                if a>=b:
                    a = a%b
                else:
                    b = b%a
            if a==0:
                return b
            else:
                return a
        if N==1:
            return arr[0]
        else:
            gcd = get_hcf(arr[0],arr[1])
            for i in range(N-2):
                gcd = get_hcf(gcd, arr[i+2])
            return gcd
