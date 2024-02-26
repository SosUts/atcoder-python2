def main():
    a, b, c = map(int, input().split())
    print(*list(range(a, b + c, c)))


if __name__ == "__main__":
    main()
