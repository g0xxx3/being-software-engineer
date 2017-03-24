def coin_change_count(arr, m, n):
    if n == 0:
        return 1
    if n < 1:
        return 0
    if m <= 0 < n:
        return 0

    return coin_change_count(arr, m - 1, n) + coin_change_count(arr, m, n - arr[m - 1])


def main():
    arr = [1,2,3]
    m = len(arr)
    print(coin_change_count(arr, m, 5))


if __name__ == '__main__':
    main()
