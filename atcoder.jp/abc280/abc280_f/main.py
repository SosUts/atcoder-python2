#!/usr/bin/env python3
# from typing import *



# def solve(N: int, M: int, Q: int, A: List[int], B: List[int], C: List[int], X: List[int], Y: List[int]) -> List[str]:
def solve(N, M, Q, A, B, C, X, Y):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M, Q = map(int, input().split())
    A = [None for _ in range(M)]
    B = [None for _ in range(M)]
    C = [None for _ in range(M)]
    X = [None for _ in range(Q)]
    Y = [None for _ in range(Q)]
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
    for i in range(Q):
        X[i], Y[i] = map(int, input().split())
    a = solve(N, M, Q, A, B, C, X, Y)
    for i in range(Q):
        print(a[i])

if __name__ == '__main__':
    main()