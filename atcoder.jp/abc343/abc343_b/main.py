#!/usr/bin/env python3
# from typing import *
import numpy as np


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())  # TODO: edit here
    ar = np.empty(shape=(N, N))
    for i in range(N):
        ar[i, :] = list(map(int, input().split()))
    for i in range(N):
        if ar[:, i].sum() != 0:
            print(*list(np.where(ar[:, i] == 1)[0] + 1))


if __name__ == "__main__":
    main()