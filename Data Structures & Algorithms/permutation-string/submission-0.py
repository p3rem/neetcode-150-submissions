class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
            
        k = len(s1)
        s1 = sorted(s1)

        for i in range(len(s2) - k + 1):
            substr = s2[i:i + k]
            if sorted(substr) == s1:
                return True 

        return False  
