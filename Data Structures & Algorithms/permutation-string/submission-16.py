class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1arr = 26*[0]
        s2arr = 26*[0]
        matches = 0

        for char in s1:
            s1arr[ord(char)-97]+=1
        for i in range(len(s1)):
            s2arr[ord(s2[i])-97]+=1
        for i in range(len(s1arr)):
            if s1arr[i] == s2arr[i]:
                matches += 1
        l = 0
        for r in range(len(s2)):
            if r >= len(s1):
                if matches == 26: return True
                
                s2arr[ord(s2[r])-97] += 1
                if s1arr[ord(s2[r])-97] == s2arr[ord(s2[r])-97]:
                    matches += 1
                elif s1arr[ord(s2[r])-97] + 1 == s2arr[ord(s2[r])-97]:
                    matches -= 1
                
                s2arr[ord(s2[l])-97] -= 1
                if s1arr[ord(s2[l])-97] == s2arr[ord(s2[l])-97]:
                    matches += 1
                elif s1arr[ord(s2[l])-97] - 1 == s2arr[ord(s2[l])-97]:
                    matches -= 1
                l+=1
        return matches == 26


        
