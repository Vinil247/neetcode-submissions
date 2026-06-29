
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        else:
            seen = {}

            for i in s:
                seen[i] = seen.get(i,0) + 1
            
            for i in t:
                seen[i] = seen.get(i,0) - 1
                if seen[i] < 0:
                    return False

            return True
