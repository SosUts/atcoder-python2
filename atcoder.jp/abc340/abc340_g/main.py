#!/usr/bin/env python3
# from typing import *

MOD = 998244353


# def solve(N: int, A: List[int], u: List[int], v: List[int]) -> int:
def solve(N, A, u, v):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    u = [None for _ in range(N - 1)]
    v = [None for _ in range(N - 1)]
    for i in range(N):
        A[i] = int(next(tokens))
    for i in range(N - 1):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, A, u, v)
    print(a)


if __name__ == "__main__":
    main()
