# ================================================================================================
# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check
# if they are one edit (or zero edits) away.
# EXAMPLE
#   pale, ple -> true
#   pales, pale -> true
#   pale, bale -> true
#   pale, bake -> false
# ================================================================================================


def is_one_away_edit(x, y):
    i = j=0
    # while i < len(x) and j < len(y):
    #     if x[i] != y[j]:



if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()
    print(is_one_away_edit(s1, s2))
