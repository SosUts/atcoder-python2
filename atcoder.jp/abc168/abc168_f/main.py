#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, A: List[int], B: List[int], C: List[int], D: List[int], E: List[int], F: List[int]) -> str:
def solve(N, M, A, B, C, D, E, F):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    A = [None for _ in range(N)]
    B = [None for _ in range(N)]
    C = [None for _ in range(N)]
    D = [None for _ in range(M)]
    E = [None for _ in range(M)]
    F = [None for _ in range(M)]
    for i in range(N):
        A[i], B[i], C[i] = map(int, input().split())
    for i in range(M):
        D[i], E[i], F[i] = map(int, input().split())
    a = solve(N, M, A, B, C, D, E, F)
    print(a)


if __name__ == "__main__":
    main()
