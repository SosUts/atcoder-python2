#!/usr/bin/env python3
# from typing import *

MOD = 1000000007


# def solve(n: int, k: int, a: List[str]) -> int:
def solve(n, k, a):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    n, k = map(int, input().split())
    a = [None for _ in range(n)]
    for i in range(n):
        a[i] = input()
    a1 = solve(n, k, a)
    print(a1)


if __name__ == "__main__":
    main()
