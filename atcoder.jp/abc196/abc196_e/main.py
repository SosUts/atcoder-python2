#!/usr/bin/env python3
# from typing import *


# def solve(N: int, a: List[int], t: List[int], Q: int, x: List[int]) -> List[str]:
def solve(N, a, t, Q, x):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    a = [None for _ in range(N)]
    t = [None for _ in range(N)]
    for i in range(N):
        a[i] = int(next(tokens))
        t[i] = int(next(tokens))
    Q = int(next(tokens))
    x = [None for _ in range(Q)]
    for i in range(Q):
        x[i] = int(next(tokens))
    assert next(tokens, None) is None
    b = solve(N, a, t, Q, x)
    for i in range(Q):
        print(b[i])


if __name__ == "__main__":
    main()
