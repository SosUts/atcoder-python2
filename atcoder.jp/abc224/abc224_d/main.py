#!/usr/bin/env python3
# from typing import *


# def solve(M: int, u: List[int], v: List[int], p: List[int]) -> int:
def solve(M, u, v, p):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    p = [None for _ in range(8)]
    import sys

    tokens = iter(sys.stdin.read().split())
    M = int(next(tokens))
    u = [None for _ in range(M)]
    v = [None for _ in range(M)]
    for i in range(M):
        u[i] = int(next(tokens))
        v[i] = int(next(tokens))
    for i in range(8):
        p[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(M, u, v, p)
    print(a)


if __name__ == "__main__":
    main()
