#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, A: List[int], B: List[int], K: int, C: List[int], D: List[int]) -> int:
def solve(N, M, A, B, K, C, D):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    A = [None for _ in range(M)]
    B = [None for _ in range(M)]
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    K = int(input())
    C = [None for _ in range(K)]
    D = [None for _ in range(K)]
    for i in range(K):
        C[i], D[i] = map(int, input().split())
    a = solve(N, M, A, B, K, C, D)
    print(a)


if __name__ == "__main__":
    main()
