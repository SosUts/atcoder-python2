#!/usr/bin/env python3
# from typing import *


# def solve(N: int, F: List[int], S: List[int]) -> int:
def solve(N, F, S):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    F = [None for _ in range(N)]
    S = [None for _ in range(N)]
    for i in range(N):
        F[i], S[i] = map(int, input().split())
    a = solve(N, F, S)
    print(a)


if __name__ == "__main__":
    main()
