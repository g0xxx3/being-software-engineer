# https://www.hackerrank.com/challenges/python-lists

if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        s = input().split()
        cmd = s[0]
        args = s[1:]

        if cmd == "print":
            print(l)
        else:
            cmd += "(" + ",".join(args) + ")"
            eval("l." + cmd)
