# ================================================================================================
# Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?
# ================================================================================================


# Solution #1: The simple way
# It can also be done using dictionary but it will have extra overhead
def is_unique_simple(s):
    if len(s) < 2:
        return True
    if len(s) > 128:
        return False

    unique_checker = [False] * 128
    for i in range(len(s)):
        val = ord(s[i])
        if unique_checker[val]:
            return False
        unique_checker[val] = True

    return True


# Solution #2: Reduce the space complexity by using bit vector
# iff the string only uses lowercase characters
def is_unique_memory_efficient(s):

    if len(s) > 26:
        return False

    checker = 0
    for i in range(len(s)):
        val = ord(s[i])
        if checker & (1 << val) > 0:
            return False
        checker |= (1 << val)

    return True


# Solution #3: If we are not allowed to create additional data structure
# we can perform the functionality in O(n^2)
def is_unique_without_data_structure(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


if __name__ == '__main__':
    input_str = input()
    print(is_unique_simple(input_str))
    print(is_unique_memory_efficient(input_str))
    print(is_unique_without_data_structure(input_str))
