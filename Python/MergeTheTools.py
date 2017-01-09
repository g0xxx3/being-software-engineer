# https://www.hackerrank.com/challenges/merge-the-tools

def merge_the_tools(string,k):
    n = len(string)
    for i in range(0,n,k):
        sliced_str = string[i:i+k]
        uni = []
        for c in sliced_str:
            if c not in uni:
                uni.append(c)
        print(''.join(uni))
    pass


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)