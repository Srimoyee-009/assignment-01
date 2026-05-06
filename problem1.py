def max_cyclic_substring_sum(s):
    n = len(s)
    s = s + s
    char_set = set()
    left = 0
    max_sum = 0
    current_sum = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            current_sum -= (ord(s[left]) - ord('a') + 1)
            left += 1

        char_set.add(s[right])
        current_sum += (ord(s[right]) - ord('a') + 1)

        if right - left + 1 <= n:
            max_sum = max(max_sum, current_sum)

    return max_sum

s = input()
print(max_cyclic_substring_sum(s))
