#!/usr/bin/env python3
# from typing import *



# def solve(N: int, A: List[int], B: List[int]) -> List[str]:
def solve(N, A, B):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    A = [None for _ in range(N)]
    B = [None for _ in range(N)]
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    X = solve(N, A, B)
    for i in range(N):
        print(X[i])

if __name__ == '__main__':
    main()
