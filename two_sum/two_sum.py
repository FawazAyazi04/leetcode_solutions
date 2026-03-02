# Solution 1 -> Brute Force

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
            


# Solution 2 -> Sorting+ two pointer

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = [(i, index) for index,i in enumerate(nums)]
        num = sorted(pairs)
        print(num)
        l = 0
        r = len(num)-1
        while l<r:
            if num[l][0] + num[r][0] > target:
                r -= 1
            elif num[l][0] + num[r][0] < target:
                l += 1
            else:
                return [num[l][1],num[r][1]]
            
# Solution 3 -> Hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}  # value:index  
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashset:
                return [hashset[diff], i]
            hashset[n] = i
        return