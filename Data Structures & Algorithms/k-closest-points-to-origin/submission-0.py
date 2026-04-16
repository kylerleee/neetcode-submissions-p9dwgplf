class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_arr = []
        for i in range(len(points)):
            dist_arr.append((math.sqrt((points[i][0])**2 + (points[i][1])**2), points[i]))
        res = []
        heapq.heapify(dist_arr)
        while k:
            k-=1
            res.append(heapq.heappop(dist_arr)[1])
        return res
