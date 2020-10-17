def modsum(a,b):
    mod = 10**9 + 7
    return (a%mod +b%mod)%mod

def bino(n,r,dict):

    if (n,r) in dict:
        return dict.get((n,r))
    if (r==0):
        dict[(n,r)] = 1
        return 1
        
    if (n==r):
        dict[(n,r)] = 1
        return 1
    else:
        sum = modsum(bino(n-1,r,dict), bino(n-1,r-1,dict))

    dict[(n,r)] = sum
    return sum

if  __name__ == "__main__":
    import sys
    # print(sys.getrecursionlimit())
    # sys.setrecursionlimit(10000)
    tests = int(input().strip())
    dict = {}
    for z in range(tests):
        p = [int(e.strip()) for e in input().split()]
        bincoef = bino(p[0],p[1],dict)
        print(bincoef)
