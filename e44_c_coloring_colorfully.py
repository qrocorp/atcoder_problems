def main():
    s = input()

    count_0 = 0
    count_1 = 0

    # begin at 0
    for i in range(len(s)):
        if i % 2 == 0:
            if int(s[i]) == 1:
                count_0 += 1
        else:
            if int(s[i]) == 0:
                count_0 += 1

    for i in range(len(s)):
        if i % 2 == 0:
            if int(s[i]) == 0:
                count_1 += 1
        else:
            if int(s[i]) == 1:
                count_1 += 1

    print(min(count_0, count_1))


if __name__ == '__main__':
    main()
