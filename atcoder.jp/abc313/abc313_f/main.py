#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, A: List[int], B: List[int], X: List[int], Y: List[int]) -> float:
def solve(N, M, A, B, X, Y):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    A = [None for _ in range(N)]
    B = [None for _ in range(N)]
    X = [None for _ in range(M)]
    Y = [None for _ in range(M)]
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        X[i], Y[i] = map(int, input().split())
    a = solve(N, M, A, B, X, Y)
    print(a)


if __name__ == "__main__":
    main()
