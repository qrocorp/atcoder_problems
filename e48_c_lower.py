def main():
    n = int(input())
    h = list(map(int, input().split()))

    max_count = 0
    count = 0

    for i in range(0, n-1):
        if h[i+1] <= h[i]:
            count += 1
            if max_count < count:
                max_count = count
        else:
            if max_count < count:
                max_count = count
            count = 0

    print(max_count)


if __name__ == '__main__':
    main()
