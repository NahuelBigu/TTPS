from sys import stdin, stdout


def rook_is_ok_at(i, j):
    if rows[i] == 1 or cols[j] == 1:
        return False
    return True


def recurse(row, numberOfRooks):
    if memo[a-row][numberOfRooks] != -1:
        return memo[a-row][numberOfRooks]
    solutions=0
    if (numberOfRooks == 0):
        return 1  
    for i in range(row, a):
        for j in range(a):
            if (rook_is_ok_at(i, j)):
                rows[i] = 1
                cols[j] = 1
                solutions +=recurse(i+1, numberOfRooks-1)
                rows[i] = -1
                cols[j] = -1
    memo[a-row][numberOfRooks] = solutions
    return solutions

N = int(stdin.readline().strip())
for cases in range(N):
    [a, b] = [int(x) for x in stdin.readline().strip().split()]
    memo = [[-1 for _ in range(a+1)] for _ in range(a+1)]
    rows = []
    cols = []
    for i in range(a):
        rows.append(-1)
        cols.append(-1)
    solutions = 0
    if a >= b:
        solutions=recurse(0, b-1)
    stdout.write("Case "+str(cases+1)+": " +
                 str(solutions)+"\n")
    
                