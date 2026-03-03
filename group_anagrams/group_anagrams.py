from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap=defaultdict(list)
        for i in strs:
            sorted_s = tuple(sorted(i))
            # print(sorted_s)
            hashmap[sorted_s].append(i)
        for mapp in hashmap.values():
            result.append(mapp)
        return sorted(result)