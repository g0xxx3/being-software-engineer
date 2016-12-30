# https://www.hackerrank.com/challenges/nested-list

if __name__ == '__main__':
    grades = [[input(), float(input())] for _ in range(int(input()))]

    second_highest = sorted(list(set([x[1] for x in grades])))[1]
    print('\n'.join([a for a, b in sorted(grades) if b == second_highest]))
