class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        val = ""
        values = self.keystore.get(key)
        l = 0
        if values == None:
            return None
        r = len(values) - 1
        print(values)
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                val = values[m][0]
                print(val)
                l = m + 1
            else:
                r = m - 1
              
        return val