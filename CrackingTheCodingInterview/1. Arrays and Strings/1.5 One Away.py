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


def one_edit_replace(x, y):
    found_difference = False

    for i in range(len(x)):
        if x[i] != y[i]:
            if found_difference:
                return False
            found_difference = True
    return True


def one_edit_insert(x, y):
    index1 = index2 = 0
    while index1 < len(x) and index2 < len(y):
        if x[index1] != y[index2]:
            if index1 == index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True


def is_one_away_edit(x, y):
    if abs(len(x) - len(y)) > 1:
        return False

    if len(x) == len(y):
        return one_edit_replace(x,y)
    elif len(x) == len(y) + 1:
        return one_edit_insert(x,y)
    elif len(x) + 1 == len(y):
        return one_edit_insert(y,x)
    return False


if __name__ == '__main__':
    s1 = input().strip()
    s2 = input().strip()

    print(is_one_away_edit(s1, s2))
