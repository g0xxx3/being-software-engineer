# ================================================================================================
#  Given two strings, write a method to decide if one is a permutation of the other.
# ================================================================================================


# We assume the character listed in ASCII set
def check_permutation(a, b):
    if len(a) != len(b):
        return False

    char_counter = [0] * 128
    for i in range(len(a)):
        val = ord(a[i])
        char_counter[val] += 1

    for i in range(len(b)):
        val = ord(b[i])
        char_counter[val] -= 1
        if char_counter[val] < 0:
            return False

    return True


if __name__ == '__main__':
    x = input().strip()
    y = input().strip()

    print(check_permutation(x, y))
