class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqdict = {}
        hf = 0
        count = 0
        hc = 0
        for char in s:
            if char in freqdict:
                freqdict[char] += 1
            else:
                freqdict[char] = 1
            count+=1
            hf = max(hf, freqdict[char])
            if count - hf > k:
                count -= 1
                freqdict[s[l]] -= 1
                l += 1
            hc = max(hc, count)
        return hc