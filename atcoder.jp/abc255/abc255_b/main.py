#!/usr/bin/env python3
# from typing import *



# def solve(N: int, K: int, A: List[int], X: List[int], Y: List[int]) -> float:
def solve(N, K, A, X, Y):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    K = int(next(tokens))
    A = [None for _ in range(K)]
    X = [None for _ in range(N)]
    Y = [None for _ in range(N)]
    for i in range(K):
        A[i] = int(next(tokens))
    for i in range(N):
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, K, A, X, Y)
    print(a)

if __name__ == '__main__':
    main()