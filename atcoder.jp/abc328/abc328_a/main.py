#!/usr/bin/env python3
# from typing import *


# def solve(N: int, X: int, S: List[int]) -> int:
def solve(N, X, S):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    X = int(next(tokens))
    S = [None for _ in range(N)]
    for i in range(N):
        S[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, X, S)
    print(a)


if __name__ == "__main__":
    main()
