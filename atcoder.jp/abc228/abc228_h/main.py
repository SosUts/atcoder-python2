#!/usr/bin/env python3
# from typing import *


# def solve(N: int, X: int, A: List[int], C: List[int]) -> int:
def solve(N, X, A, C):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, X = map(int, input().split())
    A = [None for _ in range(N)]
    C = [None for _ in range(N)]
    for i in range(N):
        A[i], C[i] = map(int, input().split())
    a = solve(N, X, A, C)
    print(a)


if __name__ == "__main__":
    main()
