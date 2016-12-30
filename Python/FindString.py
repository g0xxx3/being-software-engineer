# https://www.hackerrank.com/challenges/find-a-string


def count_substring(text, sub_text):
    total = 0
    for i in range(len(text) - len(sub_text) + 1):
        if text[i:i + len(sub_text)] == sub_text:
            total += 1
    return total


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
