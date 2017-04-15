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


def make_urlify(url_string, true_length):
    space_count = url_string[:true_length].count(' ')

    index = true_length + space_count * 2
    for i in range(true_length - 1, -1, -1):
        if url_string[i] == ' ':
            url_string[index - 1] = '0'
            url_string[index - 2] = '2'
            url_string[index - 3] = '%'
            index -= 3
        else:
            url_string[index - 1] = url_string[i]
            index -= 1

    return ''.join(url_string)

def build_app():
    input_string = input()
    string_length = int(input().strip())
    print(make_urlify(list(input_string), string_length))

if __name__ == '__main__':
    build_app()
