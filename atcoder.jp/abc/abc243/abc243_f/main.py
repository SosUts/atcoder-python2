#!/usr/bin/env python3
# from typing import *

MOD = 998244353


# def solve(N: int, M: int, K: int, W: List[int]) -> int:
def solve(N, M, K, W):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M, K = map(int, input().split())
    W = [None for _ in range(N)]
    for i in range(N):
        W[i] = int(input())
    a = solve(N, M, K, W)
    print(a)


if __name__ == "__main__":
    main()