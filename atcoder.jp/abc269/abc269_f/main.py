#!/usr/bin/env python3
# from typing import *

MOD = 998244353


# def solve(N: int, M: int, Q: int, A: List[int], B: List[int], C: List[int], D: List[int]) -> List[str]:
def solve(N, M, Q, A, B, C, D):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    Q = int(input())
    A = [None for _ in range(Q)]
    B = [None for _ in range(Q)]
    C = [None for _ in range(Q)]
    D = [None for _ in range(Q)]
    for i in range(Q):
        A[i], B[i], C[i], D[i] = map(int, input().split())
    a = solve(N, M, Q, A, B, C, D)
    for i in range(Q):
        print(a[i])


if __name__ == "__main__":
    main()
