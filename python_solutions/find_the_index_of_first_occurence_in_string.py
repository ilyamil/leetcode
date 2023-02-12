def strStr(haystack: str, needle: str) -> int:
    if len(needle) > len(haystack):
        return -1

    left = 0
    right = len(needle)
    while right < len(haystack) + 1:
        if needle == haystack[left: right]:
            return left
        left += 1
        right += 1
    return -1


if __name__ == '__main__':
    # haystack = "sadbutsad"
    # needle = "sad"
    haystack = "sadbutsad"
    needle = "tsad"
    ans = strStr(haystack, needle)
    print(ans)
