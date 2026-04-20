class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res, reslen = [-1,-1], float("infinity")
        l = 0
        tmap, smap = {}, {}
        
        for i in t:
            tmap[i] = 1 + tmap.get(i, 0)
        
        have, need = 0, len(tmap)

        for r in range(len(s)):
            if s[r] in tmap:
                smap[s[r]] = 1 + smap.get(s[r], 0)

            if s[r] in tmap and smap[s[r]] == tmap[s[r]]:
                have+=1
            
            while have == need:
                if s[l] in smap:
                    smap[s[l]] -= 1
                    if smap[s[l]] < tmap[s[l]]:
                        have -= 1
                        if (r - l + 1) < reslen:
                            res = [l,r]
                            reslen = r - l + 1
                l+=1

        l,r = res

        return s[l:r+1] if reslen != float("infinity") else ""
