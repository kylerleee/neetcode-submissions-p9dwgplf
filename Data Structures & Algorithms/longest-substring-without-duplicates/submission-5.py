class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        i = 0
        highest = 0
        if len(s) <= 1:
            return len(s)

        while i < len(s):
            if s[i] not in dic.keys():
                dic[s[i]] = i
                i += 1
            else:
                highest = max(highest, i)
                s = s[dic[s[i]]+1:]
                dic = {}
                i = 0

        return max(highest, i)

