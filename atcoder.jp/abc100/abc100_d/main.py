#!/usr/bin/env python3
# from typing import *



# def solve(a: int, b: int, c: List[int], d: List[int], e: List[int]) -> int:
def solve(a, b, c, d, e):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    a, b = map(int, input().split())
    c = [None for _ in range(a)]
    d = [None for _ in range(a)]
    e = [None for _ in range(a)]
    for i in range(a):
        c[i], d[i], e[i] = map(int, input().split())
    a1 = solve(a, b, c, d, e)
    print(a1)

if __name__ == '__main__':
    main()