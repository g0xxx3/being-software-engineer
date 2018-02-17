# Decompress string - string (s) followed by {n} denotes s repeating n times
# "a(b(c){2}){2}d" decompresses to "abccbccd"
# "((x){3}(y){2}z){2}" decompresses to "xxxyyzxxxyyz"


class StringDecompressor:
    def __init__(self):
        self.stack = []

    def decompress(self, text):
        self.stack = []
        current_text = []
        for ch in text:
            # end of the character sequence
            if ch == ')':
                current_text += self.get_text()
            # end of the multiplier sequence
            elif ch == '}':
                self.stack += current_text * self.get_multiplier()
                current_text = []
            else:
                self.stack.append(ch)

        return ''.join(self.stack)

    def get_text(self):
        substring = []
        while True:
            ch = self.stack.pop()
            if ch == '(':
                break
            substring.append(ch)
        return reversed(substring)

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
    print(stringDecompressor.decompress('a(b(c){2}){2}d'))
    print(stringDecompressor.decompress('((x){3}(y){2}z){2}'))
    print(stringDecompressor.decompress('x((x){3}(y){2}z){2}'))
    print(stringDecompressor.decompress('x((x){3}(y){2}z){2}z'))
