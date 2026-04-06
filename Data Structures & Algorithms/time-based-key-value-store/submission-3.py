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
        for val in store:
            if val[1] == timestamp:
                return val[0]
        for val in store[::-1]:
            if val[1] < timestamp:
                return val[0]
        
        return ""
           