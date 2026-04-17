class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        count =  1
        
        for i in range(len(s)):
            current_substring = s[i]
            for j in range(i+1,len(s)):
                if s[j] not in current_substring:
                    current_substring += s[j]
                    count = max(len(current_substring),count)
                else:
                    break
        return count 