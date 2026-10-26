class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for char in s:
                index = ord(char) - ord('a')
                count[index] += 1
            counttuple = tuple(count)
            res[counttuple].append(s)
        
        reslist = list(res.values())
        return reslist
        