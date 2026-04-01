class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        harris = []
        big_sean = {}
        for i,word in enumerate(strs):
            harris26sixseven = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            for letter in word:
                harris26sixseven[ord(letter) - 97] += 1
            if tuple(harris26sixseven) in big_sean:
                big_sean[tuple(harris26sixseven)].append(word)
            else:
                big_sean[tuple(harris26sixseven)] = [word]
        
        for key, value in big_sean.items():
            harris.append(value)
            
        return harris
