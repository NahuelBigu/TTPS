import sys
sys.setrecursionlimit(20000000)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a):
    if (dp[a] != -1):
        return dp[a]
    if (a<1):
        return 1
    dp[a]= (a*lcm(a-1)) / (gcd(a,lcm(a-1)))
    return dp[a]


n=int(stdin.readline().strip())
while (n != 0):
    print(str(lcm(n)).strip("0")[-1:])
    n=int(stdin.readline().strip())
    
dp = [-1] * (10+2)
print(int(lcm(10)))
print(str(int(lcm(10))).strip("0")[-1:])