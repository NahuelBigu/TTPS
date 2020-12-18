from sys import stdin,stdout


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


cases = int(stdin.readline().strip())
for _ in range(cases):
    a,b=[int(x) for x in stdin.readline().strip().split()]
    print(gcd(a,b))