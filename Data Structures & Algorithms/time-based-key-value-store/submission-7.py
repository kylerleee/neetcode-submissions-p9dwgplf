class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.map:
            store = self.map[key]
        else:
            return ""
        print(store)

        l, r = 0, len(store) - 1
        walao = False
        while l <= r:
            m = l + (r-l) // 2
            if store[m][1] == timestamp:
                return store[m][0]
            elif store[m][1] < timestamp:
                l = m + 1
                something = m
                walao = True
            else:
                r = m - 1
        
        if walao:
            return store[something][0]
        else:
            return ""
           