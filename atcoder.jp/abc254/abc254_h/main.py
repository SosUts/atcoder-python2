#!/usr/bin/env python3
# from typing import *


# def solve(N: int, a: List[int], b: List[int]) -> int:
def solve(N, a, b):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    a = [None for _ in range(N)]
    b = [None for _ in range(N)]
    for i in range(N):
        a[i] = int(next(tokens))
    for i in range(N):
        b[i] = int(next(tokens))
    assert next(tokens, None) is None
    a1 = solve(N, a, b)
    print(a1)


if __name__ == "__main__":
    main()
