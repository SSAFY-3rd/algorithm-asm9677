import sys
sys.setrecursionlimit(10**6)
def solve(s):
    if len(s) == len(S):
        return s == S
    return solve(s[:-1]) if s[-1] == 'A' else solve(s[-2::-1])
S,T = input(),input()
print(solve(T)+0)