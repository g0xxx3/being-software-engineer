from collections import defaultdict

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    visited = defaultdict(int)
    max_length = 0
    i = 0

    for j in range(len(s)):
        if s[j] in visited:
            if visited[s[j]] < i:
                visited[s[j]] = j
            else:
                max_length = max(max_length, j - i)
                i = visited[s[j]] + 1

        visited[s[j]] = j

    max_length = max(max_length, j - i + 1)
    return max_length

print(lengthOfLongestSubstring('abcabcd'))
