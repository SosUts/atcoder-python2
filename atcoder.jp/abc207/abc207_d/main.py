#!/usr/bin/env python3
# from typing import *

YES = "Yes"
NO = "No"


# def solve(N: int, a: List[int], b: List[int], c: List[int], d: List[int]) -> str:
def solve(N, a, b, c, d):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    a = [None for _ in range(N)]
    b = [None for _ in range(N)]
    c = [None for _ in range(N)]
    d = [None for _ in range(N)]
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    for i in range(N):
        c[i], d[i] = map(int, input().split())
    a1 = solve(N, a, b, c, d)
    print(a1)


if __name__ == "__main__":
    main()
