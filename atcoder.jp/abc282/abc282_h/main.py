#!/usr/bin/env python3
# from typing import *


# def solve(N: int, S: int, A: List[int], B: List[int]) -> int:
def solve(N, S, A, B):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    S = int(next(tokens))
    A = [None for _ in range(N)]
    B = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    for i in range(N):
        B[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, S, A, B)
    print(a)


if __name__ == "__main__":
    main()
