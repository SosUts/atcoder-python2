#!/usr/bin/env python3
# from typing import *

YES = "Yes"
NO = "No"


# def solve(W: int, B: int) -> str:
def solve(W, B):
    """
    一回の繰り返しで7w5b増える
    """
    rep = min((W // 7, B // 5))
    count_w = W - 7 * rep
    count_b = B - 5 * rep
    for s in "wbwbwwbwbwbw":
        if s == "w":
            count_w -= 1
        else:
            count_b -= 1
        if count_w == 0 and count_b == 0:
            return YES
    return NO


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    W, B = map(int, input().split())
    a = solve(W, B)
    print(a)


if __name__ == "__main__":
    main()