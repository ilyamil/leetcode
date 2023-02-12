from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    key_to_group = {}
    for s in strs:
        s_ = ''.join(sorted(s))
        if s_ in key_to_group.keys():
            key_to_group[s_].append(s)
        else:
            key_to_group[s_] = [s]
    return list(key_to_group.values())


if __name__ == '__main__':
    # strs = ["eat","tea","tan","ate","nat","bat"]
    # ans = groupAnagrams(strs)
    # expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
    strs = [""]
    ans = groupAnagrams(strs)
    expected = [[""]]
    print(ans, expected)