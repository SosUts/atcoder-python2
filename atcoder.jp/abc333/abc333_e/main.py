#!/usr/bin/env python3
# from typing import *


# def solve(N: int, t: List[int], x: List[int]) -> Any:
def solve(N, t, x):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    t = [None for _ in range(N)]
    x = [None for _ in range(N)]
    for i in range(N):
        t[i], x[i] = map(int, input().split())
    ans = solve(N, t, x)
    print(ans)  # TODO: edit here


if __name__ == "__main__":
    main()
