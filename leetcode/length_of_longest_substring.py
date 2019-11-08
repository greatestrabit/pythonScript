def lengthOfLongestSubstring(s: str):
    temp_set = []
    start = 0
    end = 1
    max = 0

    while end < len(s):
        if s[end - 1: end] not in temp_set:
            temp_set.append(s[end - 1:end])
            end = end + 1
            print(temp_set)
            if max < len(temp_set):
                max = len(temp_set)
        else:
            temp_set.remove(s[start: start + 1])
            start = start + 1

    print(max)


lengthOfLongestSubstring('abcabcbb')
