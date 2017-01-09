# https://www.hackerrank.com/challenges/the-minion-game


def minion_game(string):
    s_score, k_score, length, vowels = 0, 0, len(string), 'AEIOU'
    for i in range(length):
        if string[i] in vowels:
            k_score += (length - i)
        else:
            s_score += (length - i)

    if k_score > s_score:
        print("Kevin", k_score)
    elif k_score < s_score:
        print("Stuart", s_score)
    else:
        print("Draw")
    pass


if __name__ == '__main__':
    s = input()
    minion_game(s)
