# Decompress string - string (s) followed by {n} denotes s repeating n times
# "a(b(c){2}){2}d" decompresses to "abccbccd"
# "((x){3}(y){2}z){2}" decompresses to "xxxyyzxxxyyz"


class StringDecompressor:
    def __init__(self):
        self.stack = []

    def decompress_string(self, text):
        result = []
        current_text = []
        for ch in text:
            if ch == ')':
                temp = self.get_text()
                temp.extend(current_text)
                current_text = temp
            elif ch == '}':
                current_text = current_text * self.get_multiplier()
            elif len(self.stack) == 0 and ch != '(' and ch != '{':
                result.extend(current_text)
                result.append(ch)
                current_text = []
            else:
                self.stack.append(ch)

        if len(current_text) != 0:
            result.extend(reversed(current_text))

        return ''.join(result)

    def get_text(self):
        substring = []
        while True:
            ch = self.stack.pop()
            if ch == '(':
                break
            substring.append(ch)
        return substring

    def get_multiplier(self):
        mult = 0
        p = 1
        while True:
            ch = self.stack.pop()
            if ch == '{':
                break
            mult += int(ch) * p
            p *= 10
        return mult


if __name__ == '__main__':
    stringDecompressor = StringDecompressor()
    print(stringDecompressor.decompress_string('a(b(c){2}){2}d'))
    print(stringDecompressor.decompress_string('((x){3}(y){2}z){2}'))
    print(stringDecompressor.decompress_string('x((x){3}(y){2}z){2}'))
    print(stringDecompressor.decompress_string('x((x){3}(y){2}z){2}z'))
