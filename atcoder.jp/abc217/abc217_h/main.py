#!/usr/bin/env python3
# from typing import *


# def solve(N: int, T: List[int], D: List[int], X: List[int]) -> int:
def solve(N, T, D, X):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    T = [None for _ in range(N)]
    D = [None for _ in range(N)]
    X = [None for _ in range(N)]
    for i in range(N):
        T[i], D[i], X[i] = map(int, input().split())
    a = solve(N, T, D, X)
    print(a)


if __name__ == "__main__":
    main()
