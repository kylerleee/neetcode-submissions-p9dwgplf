class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        max_fleet = len(position)

        for i in range(len(pair)):
            curr = i+1
            while curr-1 < len(pair) - 1:
                factor = (target-pair[i][0]) / pair[i][1]
                next_factor = (target-pair[curr][0]) / pair[curr][1]
                if factor >= next_factor:
                    pair.pop(curr)
                    max_fleet -=1
                else:
                    curr+=1
        
        return max_fleet



        

            
        