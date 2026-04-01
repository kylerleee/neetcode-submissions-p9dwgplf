class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        for i, letter in enumerate(s):
            if letter in seen1:
                seen1[letter] += 1
            else:
                seen1[letter] = 1

        seen2 = {}
        for i, letter in enumerate(t):
            if letter in seen2:
                seen2[letter] += 1
            else:
                seen2[letter] = 1
                
        return seen1==seen2