# Time Complexity: O(n*n!)
def permute_string_backtrack(a, l, r):
    if l == r:
        print(''.join(a))
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute_string_backtrack(a, l + 1, r)
            a[l], a[i] = a[i], a[l]


if __name__ == '__main__':
        s = "Hello"
        permute_string_backtrack(list(s), 0, len(s))
