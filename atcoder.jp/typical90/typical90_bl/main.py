#!/usr/bin/env python3
# from typing import *



# def solve(N: int, Q: int, A: List[int], L: List[int], R: List[int], V: List[int]) -> List[str]:
def solve(N, Q, A, L, R, V):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    Q = int(next(tokens))
    A = [None for _ in range(N)]
    L = [None for _ in range(Q)]
    R = [None for _ in range(Q)]
    V = [None for _ in range(Q)]
    for i in range(N):
        A[i] = int(next(tokens))
    for i in range(Q):
        L[i] = int(next(tokens))
        R[i] = int(next(tokens))
        V[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, Q, A, L, R, V)
    for i in range(Q):
        print(a[i])

if __name__ == '__main__':
    main()
