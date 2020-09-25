def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    min_p = p[0]
    for i in range(n):
        if min_p > p[i]:
            min_p = p[i]
        if p[i] <= min_p:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
