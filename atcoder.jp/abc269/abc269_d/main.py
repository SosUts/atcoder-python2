#!/usr/bin/env python3
# from typing import *


# def solve(N: int, X: List[int], Y: List[int]) -> int:
def solve(N, X, Y):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    X = [None for _ in range(N)]
    Y = [None for _ in range(N)]
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    a = solve(N, X, Y)
    print(a)


if __name__ == "__main__":
    main()
