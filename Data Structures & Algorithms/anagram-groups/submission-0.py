class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict

        group = defaultdict(list)

        for i in strs:
            group["".join(sorted(i))].append(i)
        return list(group.values())
            