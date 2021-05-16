class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, v in enumerate(nums):
            if v in indices:
                return [indices[v], i]
            else:
                indices[target - v] = i
