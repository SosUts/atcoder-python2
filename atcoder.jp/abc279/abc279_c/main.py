#!/usr/bin/env python3
# from typing import *

YES = "Yes"
NO = "No"


# def solve(H: int, W: int, S: List[str], T: List[str]) -> str:
def solve(H, W, S, T):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    H, W = map(int, input().split())
    S = [None for _ in range(H)]
    T = [None for _ in range(H)]
    for i in range(H):
        S[i] = input()
    for i in range(H):
        T[i] = input()
    a = solve(H, W, S, T)
    print(a)


if __name__ == "__main__":
    main()
