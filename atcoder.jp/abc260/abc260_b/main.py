#!/usr/bin/env python3
# from typing import *


# def solve(N: int, X: int, Y: int, Z: int, A: List[int], B: List[int]) -> Tuple[List[str], List[str], str]:
def solve(N, X, Y, Z, A, B):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    X = int(next(tokens))
    Y = int(next(tokens))
    Z = int(next(tokens))
    A = [None for _ in range(N)]
    B = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    for i in range(N):
        B[i] = int(next(tokens))
    assert next(tokens, None) is None
    d, e, f = solve(N, X, Y, Z, A, B)
    for i in range(X):
        print(d[i])
        print(e[i])
    print(f)


if __name__ == "__main__":
    main()
