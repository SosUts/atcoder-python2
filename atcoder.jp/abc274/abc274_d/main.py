#!/usr/bin/env python3
# from typing import *

YES = "Yes"
NO = "No"


# def solve(N: int, x: int, y: int, A: List[int]) -> str:
def solve(N, x, y, A):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    x = int(next(tokens))
    y = int(next(tokens))
    A = [None for _ in range(N)]
    for i in range(N):
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, x, y, A)
    print(a)


if __name__ == "__main__":
    main()
