#!/usr/bin/env python3
# from typing import *


# def solve(N: int, a: List[int], b: List[int], Q: int, t: List[int], e: List[int], x: List[int]) -> List[str]:
def solve(N, a, b, Q, t, e, x):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    a = [None for _ in range(N - 1)]
    b = [None for _ in range(N - 1)]
    for i in range(N - 1):
        a[i], b[i] = map(int, input().split())
    Q = int(input())
    t = [None for _ in range(Q)]
    e = [None for _ in range(Q)]
    x = [None for _ in range(Q)]
    for i in range(Q):
        t[i], e[i], x[i] = map(int, input().split())
    ans = solve(N, a, b, Q, t, e, x)
    for i in range(N):
        print(ans[i])


if __name__ == "__main__":
    main()
