# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int(input())
    arr = [int(x) for x in input().split()]
    p_max, s_max = [-111, -111]

    for x in arr:
        if x > p_max and x > s_max:
            s_max = p_max
            p_max = x
        elif x != p_max and x > s_max:
            s_max = x

    print(s_max)
