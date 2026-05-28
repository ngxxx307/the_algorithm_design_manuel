class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        set1 = [0] * 26
        set2 = [0] * 26

        for i in range(len(s1)):
            set1[ord(s1[i]) - ord("a")] += 1
            set2[ord(s2[i]) - ord("a")] += 1

        matches = 0
        for i in range(26):
            if set1[i] == set2[i]:
                matches += 1
        if matches == 26:
            return True

        for i in range(len(s1), len(s2)):
            lc = s2[i - len(s1)]
            rc = s2[i]
            if rc == lc:
                continue

            l = ord(lc) - ord("a")
            set2[l] -= 1

            if set2[l] == set1[l]:
                matches += 1
            if set2[l] + 1 == set1[l]:
                matches -= 1

            r = ord(rc) - ord("a")
            set2[r] += 1
            if set2[r] == set1[r]:
                matches += 1
            if set2[r] - 1 == set1[r]:
                matches -= 1

            if matches == 26:
                return True

        return False
