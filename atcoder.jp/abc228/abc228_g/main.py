#!/usr/bin/env python3
# from typing import *

MOD = 998244353


# def solve(H: str, W: str, N: str, c: List[List[str]]) -> int:
def solve(H, W, N, c):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    H = next(tokens)
    W = next(tokens)
    N = next(tokens)
    c = [[None for _ in range(H + W + 4)] for _ in range(H + W + 4)]
    for j in range(H + 4):
        for i in range(W):
            c[i + j][i + j] = next(tokens)
    assert next(tokens, None) is None
    a = solve(H, W, N, c)
    print(a)


if __name__ == "__main__":
    main()
