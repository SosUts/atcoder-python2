#!/usr/bin/env python3
# from typing import *


# def solve(N: str, M: str, p: List[str], S: List[str]) -> Tuple[int, int]:
def solve(N, M, p, S):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = input().split()
    p = [None for _ in range(M)]
    S = [None for _ in range(M)]
    for i in range(M):
        p[i], S[i] = input().split()
    c, d = solve(N, M, p, S)
    print(c, d)


if __name__ == "__main__":
    main()
