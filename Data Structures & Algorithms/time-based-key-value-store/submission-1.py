class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        ar = self.map[key]
        l, r = 0, len(ar) - 1
        res = ""
        while l<=r:
            mid = l + (r-l)//2
            if ar[mid][0]<=timestamp:
                res = ar[mid][1]
                l = mid + 1
            else:
                r = mid -1
        return res
        
