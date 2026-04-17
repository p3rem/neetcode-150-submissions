class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for _ in nums:
            if _ in seen:
                return _
            seen.add(_)
        