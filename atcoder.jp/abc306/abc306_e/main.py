#!/usr/bin/env python3
# from typing import *


# def solve(N: int, K: int, Q: int, X: List[int], Y: List[int]) -> List[str]:
def solve(N, K, Q, X, Y):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, K, Q = map(int, input().split())
    X = [None for _ in range(Q)]
    Y = [None for _ in range(Q)]
    for i in range(Q):
        X[i], Y[i] = map(int, input().split())
    a = solve(N, K, Q, X, Y)
    for i in range(Q):
        print(a[i])


if __name__ == "__main__":
    main()
