#!/usr/bin/env python3
# from typing import *

YES = "Yes"
NO = "No"


# def solve(N: int, A: int, B: int, C: int, s: List[str]) -> Any:
def solve(N, A, B, C, s):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, A, B, C = map(int, input().split())
    s = [None for _ in range(N)]
    for i in range(N):
        s[i] = input()
    ans = solve(N, A, B, C, s)
    print(ans)  # TODO: edit here


if __name__ == "__main__":
    main()
