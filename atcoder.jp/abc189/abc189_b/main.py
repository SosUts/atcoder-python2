#!/usr/bin/env python3
# from typing import *


# def solve(N: int, X: int, V: List[int], P: List[int]) -> int:
def solve(N, X, V, P):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, X = map(int, input().split())
    V = [None for _ in range(N)]
    P = [None for _ in range(N)]
    for i in range(N):
        V[i], P[i] = map(int, input().split())
    a = solve(N, X, V, P)
    print(a)


if __name__ == "__main__":
    main()
