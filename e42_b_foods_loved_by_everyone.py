def main():
    n, m = map(int, input().split())
    l = list(range(1, m+1))
    print(l)
    for i in range(n):
        ul = list(map(int, input().split()))
        for j in range(len(l)):
            if l[j] not in ul[1:]:
                l[j] = 0
    print(len(l) - l.count(0))


if __name__ == '__main__':
    main()
