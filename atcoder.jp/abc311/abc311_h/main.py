#!/usr/bin/env python3
# from typing import *


# def solve(N: int, X: int, P: List[int], B: List[int], W: List[int], C: List[int]) -> List[str]:
def solve(N, X, P, B, W, C):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    X = int(next(tokens))
    P = [None for _ in range(N - 1)]
    B = [None for _ in range(N)]
    W = [None for _ in range(N)]
    C = [None for _ in range(N)]
    for i in range(N - 1):
        P[i] = int(next(tokens))
    for i in range(N):
        B[i] = int(next(tokens))
        W[i] = int(next(tokens))
        C[i] = int(next(tokens))
    assert next(tokens, None) is None
    ans = solve(N, X, P, B, W, C)
    for i in range(N):
        print(ans[i])


if __name__ == "__main__":
    main()
