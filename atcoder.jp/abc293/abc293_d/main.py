#!/usr/bin/env python3
# from typing import *


# def solve(N: str, M: str, A: List[str], B: List[str], C: List[str], D: List[str]) -> Tuple[int, int]:
def solve(N, M, A, B, C, D):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = input().split()
    A = [None for _ in range(M)]
    B = [None for _ in range(M)]
    C = [None for _ in range(M)]
    D = [None for _ in range(M)]
    for i in range(M):
        A[i], B[i], C[i], D[i] = input().split()
    c, d = solve(N, M, A, B, C, D)
    print(c, d)


if __name__ == "__main__":
    main()
