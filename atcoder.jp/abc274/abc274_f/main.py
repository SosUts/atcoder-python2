#!/usr/bin/env python3
# from typing import *


# def solve(N: int, A: int, W: List[int], X: List[int], V: List[int]) -> int:
def solve(N, A, W, X, V):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, A = map(int, input().split())
    W = [None for _ in range(N)]
    X = [None for _ in range(N)]
    V = [None for _ in range(N)]
    for i in range(N):
        W[i], X[i], V[i] = map(int, input().split())
    a = solve(N, A, W, X, V)
    print(a)


if __name__ == "__main__":
    main()
