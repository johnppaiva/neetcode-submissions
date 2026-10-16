class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:

        values = self.keystore.get(key,[])

        l = 0
        r = len(values) - 1
        out = ""
        while l <= r:
            m = l + (r - l) // 2

            if timestamp >= values[m][1]:
                out = values[m][0]
                l += 1
            else:
                r -= 1
        
        return out

        
