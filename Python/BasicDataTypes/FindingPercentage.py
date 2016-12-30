# https://www.hackerrank.com/challenges/finding-the-percentage

if __name__ == '__main__':
    grades = {name: (float(m) + float(p) + float(c))/3 for name, m, p, c in [input().split() for _ in range(int(input()))]}
    print("%.2f" % grades[input()])
