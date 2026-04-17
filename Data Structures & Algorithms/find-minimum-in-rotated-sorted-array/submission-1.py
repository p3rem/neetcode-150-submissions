class Solution:
    def findMin(self, nums: List[int]) -> int:
        minv = nums[0]
        for x in nums:
            if x < minv:
                minv = x
        return minv
        