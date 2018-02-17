def sort_array(items):
    count_0 = items.count(0)
    result = [0 for _ in range(count_0)]
    result.extend([1 for _ in range(len(items) - count_0)])
    return result


if __name__ == '__main__':
    print(sort_array([1, 0, 0, 0, 1, 0, 1, 1, 1, 1]))
    print(sort_array([1, 0, 0, 1, 1, 0, 1, 1, 1, 1]))
