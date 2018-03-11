# https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/


def find_max_sum(a):
    sum_odd = sum_even = 0
    max_sum = 0
    for i in range(len(a)):
        if i % 2:
            sum_even += a[i]
            if sum_even > max_sum:
                max_sum = sum_even
        else:
            sum_odd += a[i]
            if sum_odd > max_sum:
                max_sum = sum_odd
    return max_sum


if __name__ == '__main__':
    print(find_max_sum([5, 5, 10, 100, 10, 5]))
    print(find_max_sum([1, 2, 3]))
    print(find_max_sum([1, 20, 3]))
    print(find_max_sum([0, 24, 5, 6, 1, 43, 423, 54, 23, 54, 22, 6, 0, 1, 4, 2, 33, 2, 4, 2, 3]))
