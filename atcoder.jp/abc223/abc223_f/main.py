#!/usr/bin/env python3
# from typing import *

YES = "Yes"
NO = "No"


# def solve(a: int, b: int, c: List[str], d: List[int], e: List[int], f: int) -> Any:
def solve(a, b, c, d, e, f):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    a = int(next(tokens))
    b = int(next(tokens))
    c = [None for _ in range(b)]
    d = [None for _ in range(b)]
    e = [None for _ in range(b)]
    for i in range(b):
        c[i] = next(tokens)
        d[i] = int(next(tokens))
        e[i] = int(next(tokens))
    f = int(next(tokens))
    assert next(tokens, None) is None
    ans = solve(a, b, c, d, e, f)
    print(ans)  # TODO: edit here


if __name__ == "__main__":
    main()
