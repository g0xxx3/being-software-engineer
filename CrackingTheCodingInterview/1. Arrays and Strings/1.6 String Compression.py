# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def compress_string(input_str):
    current_chr = input_str[0]
    current_count = 1

    result_str = []
    for i in range(1, len(input_str)):
        if current_chr == input_str[i]:
            current_count += 1
        else:
            result_str.append(current_chr)
            result_str.append(str(current_count))
            current_chr = input_str[i]
            current_count = 1

    result_str.append(current_chr)
    result_str.append(str(current_count))

    if len(result_str) < len(input_str):
        return result_str
    return input_str

if __name__ == '__main__':
    s1 = input().strip()
    print(''.join(compress_string(s1)))
