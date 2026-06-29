class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        if len(s) != len(t):
            return False
        else:
            seen = defaultdict(int) 

            for i in s:
                seen[i] += 1

            for i in t:
                seen[i] -= 1

                if seen[i] < 0:
                    return False
            return True
