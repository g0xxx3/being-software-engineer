
def edit_distance(str1, str2,m,n):
    if m == 0:
        return n
    if n == 0:
        return m
    if str1[m - 1] == str2[n-1]:
        return edit_distance(str1, str2, m-1, n-1)
    return 1 + min(
                    edit_distance(str1, str2, m, n - 1), # insert
                    edit_distance(str1, str2, m - 1, n), # remove
                    edit_distance(str1, str2, m - 1, n - 1) # replace
                   )

def main():
    str1 = "sunday"
    str2 = "saturday"
    print("Length of Minimum Edit Distance is", edit_distance(str1, str2, len(str1), len(str2)))


if __name__ == '__main__':
    main()