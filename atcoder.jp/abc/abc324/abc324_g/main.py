#!/usr/bin/env python3
# from typing import *


# def solve(N: int, A: List[int], Q: int, t: List[int], s: List[int], x: List[int]) -> List[str]:
def solve(N, A, Q, t, s, x):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    Q = int(next(tokens))
    t = [None for _ in range(Q)]
    s = [None for _ in range(Q)]
    x = [None for _ in range(Q)]
    for i in range(Q):
        t[i] = int(next(tokens))
        s[i] = int(next(tokens))
        x[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, A, Q, t, s, x)
    for i in range(Q):
        print(a[i])


if __name__ == "__main__":
    main()