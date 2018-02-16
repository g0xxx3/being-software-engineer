def reverse_string(text):
    items = [ord(ch) for ch in text]
    for i in range(len(items)/2):
        items[i] ^= items[len(items) - i - 1]
        items[len(items) - i - 1] ^= items[i]
        items[i] ^= items[len(items) - i - 1]
    return ''.join([chr(ch) for ch in items])


if __name__ == '__main__':
    print(reverse_string('abcdef  hello'))
    print(reverse_string('abcdefg  hello'))
