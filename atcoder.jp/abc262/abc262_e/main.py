#!/usr/bin/env python3
# from typing import *

MOD = 998244353


# def solve(N: int, M: int, K: int, U: List[int], V: List[int]) -> int:
def solve(N, M, K, U, V):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M, K = map(int, input().split())
    U = [None for _ in range(M)]
    V = [None for _ in range(M)]
    for i in range(M):
        U[i], V[i] = map(int, input().split())
    a = solve(N, M, K, U, V)
    print(a)


if __name__ == "__main__":
    main()
