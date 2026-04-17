class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq  ={}
        for num in nums:
            if freq.get(num,0) == 1:
                return True 
            else:
                freq[num] = 1
        return False 
