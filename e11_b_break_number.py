def main():
    n = int(input())

    power = 0

    while 2 ** power <= n:
        power += 1

    print(2 ** (power-1))


if __name__ == "__main__":
    main()
