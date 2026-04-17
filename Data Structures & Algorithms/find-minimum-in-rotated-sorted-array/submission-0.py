class Solution:
    def findMin(self, nums: List[int]) -> int:
        minv = nums[0]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] < minv:
                    minv = nums[j]
        return minv


        