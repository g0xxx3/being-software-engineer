# ================================================================================================
# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same  forwards and backwards.
# A permutation is a rearrangement of letters. The palindrome does not need to be limited
# to just dictionary words.
# EXAMPLE
#   Input: tact coa
#   Output: True (permutations: "taco cat", "atco eta", etc.)
# ================================================================================================


def check_palindrome_permutation(phrase):
    bit_vector = create_bit_vector(phrase)
    return bit_vector == 0 or check_only_one_set_bit(bit_vector)


def create_bit_vector(phrase):
    bit_vector = 0
    for c in phrase:
        bit_vector = toggle_bit_vector(bit_vector, get_char_number(c))

    return bit_vector


def toggle_bit_vector(bit_vector, index):
    if index < 0:
        return bit_vector

    mask = 1 << index
    if bit_vector & mask == 0:
        bit_vector |= mask
    else:
        bit_vector &= ~mask

    return bit_vector


def get_char_number(c):
    return ord(c) - ord('a')


def check_only_one_set_bit(bit_vector):
    return (bit_vector & (bit_vector - 1)) == 0


if __name__ == '__main__':
    input_str = input().strip()
    print(check_palindrome_permutation(input_str))
