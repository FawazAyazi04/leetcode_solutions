# Solution 1 -> Hashmap

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hashmap = {}
        result =""
        for i,word in enumerate(strs):
            # BUild hashmap first
            if i == 0:
                for index,j in enumerate(word):
                    hashmap[index] = j
                continue
            new_limit = 0
            for index,j in enumerate(word):
                if index not in hashmap or hashmap[index] != j:
                    break
                new_limit+=1
            hashmap = {k: hashmap[k] for k in range(new_limit)} 
        for index in sorted(hashmap.keys()):
            result += hashmap[index]

        return result
    
#  Solution 2 -> list traversal

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s)  or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res