class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        search = True
        if nums[i] > target: return 0
        if nums[j] < target: return j + 1
        while search:
            if j <= i: search = False
            if nums[i] == target: return i
            if nums[j] == target: return j
            mid = int(fsum([j - i]))
            if nums[mid] == target: return mid
            if nums[mid] > target: j = mid - 1
            else: i = mid + 1
        return i
