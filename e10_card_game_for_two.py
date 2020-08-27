def main():
    n = int(input())
    a = list(map(int, input().split()))
    score = [0, 0]
    sort_a = sorted(a, reverse=True)

    for i in range(n):
        if i >= 2:
            sub_i = i % 2
        else:
            sub_i = i
        score[sub_i] += sort_a[i]

    print(score[0] - score[1])


if __name__ == "__main__":
    main()
