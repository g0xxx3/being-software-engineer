def lis(arr, n):
    lis_length = [1] * n
    max_length = 1
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j] and lis_length[i] < lis_length[j] + 1:
                lis_length[i] = lis_length[j] + 1
                max_length = max(max_length, lis_length[i])

    return max_length


def main():
    arr = [10, 22, 1, 33, 2, 50, 3, 60, 4, 5, 6, 7]
    n = len(arr)
    print("Length of LIS is", lis(arr, n))


if __name__ == '__main__':
    main()
