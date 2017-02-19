global max_lis_length


def _lis(arr, n):
    global max_lis_length
    if n == 1:
        return 1

    current_lis_length = 1

    for i in range(n):
        subproblem_lis_length = _lis(arr, i)
        if arr[i] < arr[n - 1] and current_lis_length < (1 + subproblem_lis_length):
            current_lis_length = 1 + subproblem_lis_length

    if max_lis_length < current_lis_length:
        max_lis_length = current_lis_length

    return current_lis_length


def lis(arr, n):
    global max_lis_length
    max_lis_length = 1
    _lis(arr, n)
    return max_lis_length


def main():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    n = len(arr)
    print("Length of LIS is", lis(arr, n))


if __name__ == '__main__':
    main()
