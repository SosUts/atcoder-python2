#!/usr/bin/env python3
# from typing import *


# def solve(N: int, u: List[int], v: List[int]) -> Any:
def solve(N, u, v):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    u = [None for _ in range(N - 1)]
    v = [None for _ in range(N - 1)]
    for i in range(N - 1):
        u[i], v[i] = map(int, input().split())
    ans = solve(N, u, v)
    print(ans)  # TODO: edit here


if __name__ == "__main__":
    main()
