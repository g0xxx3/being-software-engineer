def is_power_of_two(val):
    return val & ~(val & (val - 1)) == val


def counting_set_bits(val):
    count = 0
    while val:
        count += val & 1
        val >>= 1

    return count


if __name__ == '__main__':
    print(is_power_of_two(16))
    print(is_power_of_two(15))
    print(is_power_of_two(2))
    print(is_power_of_two(3))
    print(is_power_of_two(17))

    print("")
    print(12 << 1)  # multiple by 2
    print(-12 >> 1)  # divide by 2

    print("")
    print(counting_set_bits(2))
    print(counting_set_bits(1))
    print(counting_set_bits(5))
    print(counting_set_bits(15))
