from collections import defaultdict


def minus_and_del(Dict: defaultdict[str, int], c: str):
    Dict[c] -= 1
    if Dict[c] == 0:
        del Dict[c]
    return


def add_and_del(Dict: defaultdict[str, int], c: str):
    Dict[c] += 1
    if Dict[c] == 0:
        del Dict[c]
    return


def find_next_l(s: str, l: int, Set: set):
    while l < len(s) and s[l] not in Set:
        l += 1
    return l


def check_dict_valid(Dict: dict[str, int]):
    for i in Dict.values():
        if i > 0:
            return False
    return True


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        Set = set(t)
        missing_dict = defaultdict(int)
        for c in t:
            missing_dict[c] += 1
        l = 0
        l = find_next_l(s, l, Set)
        if l > len(s) - 1:
            return ""
        minus_and_del(missing_dict, s[l])
        if check_dict_valid(missing_dict):
            return s[l]

        r = l + 1
        ans = ""
        shortest = 99999999
        while l < len(s) and r < len(s):
            c = s[r]
            if s[r] in Set:
                minus_and_del(missing_dict, s[r])
                while check_dict_valid(missing_dict) and l < len(s):
                    length = r - l + 1
                    if length < shortest:
                        shortest = length
                        ans = s[l : r + 1]
                    add_and_del(missing_dict, s[l])
                    l = find_next_l(s, l + 1, Set)

            r = r + 1
        return ans