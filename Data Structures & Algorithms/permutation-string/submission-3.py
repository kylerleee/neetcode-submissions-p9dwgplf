class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        idk = {}
        for char in s1:
            if char not in idk:
                idk[char] = 1
            else:
                idk[char] += 1
        idk2 = {}
        count = 0
        l = 0
        for r in range(len(s2)):
            if s2[r] not in idk2:
                idk2[s2[r]] = 1
            else:
                idk2[s2[r]] += 1
            count+=1
            if count > len(s1):
                if idk2[s2[l]] > 1:
                    idk2[s2[l]] -= 1
                else:
                    idk2.pop(s2[l])
                l+=1
            
            if idk2 == idk:
                return True
        print(idk)
        print(idk2)
        return False

        
        