#!/usr/bin/env python3
# from typing import *

FIRST = "alice"
SECOND = "bob"


# def solve(N: int, S: List[str], A: List[int]) -> List[str]:
def solve(N, S, A):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    S = [None for _ in range(N)]
    A = [None for _ in range(N)]
    for i in range(N):
        S[i] = next(tokens)
        A[i] = int(next(tokens))
    assert next(tokens, None) is None
    ans = solve(N, S, A)
    for i in range(N):
        print(ans[i])


if __name__ == "__main__":
    main()
