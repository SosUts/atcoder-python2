#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, S: str, C: List[int]) -> str:
def solve(N, M, S, C):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    M = int(next(tokens))
    C = [None for _ in range(N)]
    S = next(tokens)
    for i in range(N):
        C[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, M, S, C)
    print(a)


if __name__ == "__main__":
    main()
