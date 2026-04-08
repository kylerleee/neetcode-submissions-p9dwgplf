class LRUCache:

    def __init__(self, capacity: int):
        self.dic = OrderedDict()
        self.c = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            self.dic.move_to_end(key, last=False)
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.dic[key] = value
        self.dic.move_to_end(key, last=False)

        if len(self.dic) > self.c:
            self.dic.popitem()

        
