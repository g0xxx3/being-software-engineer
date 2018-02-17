# https://www.geeksforgeeks.org/segregate-even-and-odd-numbers/
def segregate_even_odd(int_array) :
    left = 0
    right = len(int_array) - 1
    while left < right:
        while int_array[left] % 2 == 0:
            left += 1
        while int_array[right] % 2 != 0:
            right -= 1
        if left < right:
            int_array[left] , int_array[right] = int_array[right], int_array[left]
            left += 1
            right -= 1
    return int_array


if __name__ == '__main__':
    print(segregate_even_odd([12, 34, 45, 9, 8, 90, 3]))
    print(segregate_even_odd([12, 34, 8, 9, 45, 91, 3, 1]))
