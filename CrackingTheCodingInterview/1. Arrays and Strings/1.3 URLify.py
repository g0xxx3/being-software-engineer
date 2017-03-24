# ================================================================================================
#  Write a method to replace all spaces in a string with '%20'. You may assume that the string
#  has sufficient space at the end to hold the additional characters, and that you are given the "true"
#  length of the string. (Note: If implementing in Java, please use a character array so that you can
#  perform this operation in place.)
#
# EXAMPLE
#   Input: "Mr John Smith     ", 13
#   Output: "Mr%20John%20Smith"
# ================================================================================================


def make_urlify(s, true_length):
    space_count = s[:true_length].count(' ')

    index = true_length + space_count * 2
    for i in range(true_length - 1, -1, -1):
        if s[i] == ' ':
            s[index - 1] = '0'
            s[index - 2] = '2'
            s[index - 3] = '%'
            index -= 3
        else:
            s[index - 1] = s[i]
            index -= 1

    return ''.join(s)


if __name__ == '__main__':
    input_str = input()
    length = int(input().strip())
    print(make_urlify(list(input_str), length))
