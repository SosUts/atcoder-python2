#!/usr/bin/env python3
# from typing import *

MOD = 998244353


# def solve(N: int, M: int, C: List[int]) -> int:
def solve(N, M, C):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    C = [None for _ in range(M)]
    for i in range(M):
        C[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, M, C)
    print(a)


if __name__ == "__main__":
    main()
