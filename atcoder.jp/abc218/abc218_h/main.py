#!/usr/bin/env python3
# from typing import *


# def solve(N: int, R: int, A: List[int]) -> int:
def solve(N, R, A):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    R = int(next(tokens))
    A = [None for _ in range(N - 1)]
    for i in range(N - 1):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, R, A)
    print(a)


if __name__ == "__main__":
    main()
