#!/usr/bin/env python3
# from typing import *


# def solve(a: int, b: int, c: List[int], d: List[int], e: int, f: List[int], g: List[int]) -> List[str]:
def solve(a, b, c, d, e, f, g):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    a = int(next(tokens))
    b = int(next(tokens))
    c = [None for _ in range(b)]
    d = [None for _ in range(b)]
    f = [None for _ in range(b)]
    g = [None for _ in range(b)]
    for i in range(b):
        c[i] = int(next(tokens))
        d[i] = int(next(tokens))
    e = int(next(tokens))
    for i in range(b):
        f[i] = int(next(tokens))
        g[i] = int(next(tokens))
    assert next(tokens, None) is None
    h = solve(a, b, c, d, e, f, g)
    for j in range(a):
        print(h[j])


if __name__ == "__main__":
    main()