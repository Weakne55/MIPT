def main():
    n = int(input())
    a = input().split(maxsplit=n)
    print(a)
    a.sort(key=lambda x: sum(map(int, x)), reverse=True)
    print(*a)


if __name__ == "__main__":
    main()