from collections import deque # queue LIFO & FIFO

# LIFO - Last in first out

# FIFO - First in first out

class MemorizingDict(dict):
    history = deque(maxlen=10)
    
    def set(self, key, value):
        self.history.append(key) # MemorizingDict.history
        self[key] = value # memDict = dict() memDict[key] = value
        
    def get_history(self):
        return self.history
    

# print(MemorizingDict.__bases__)
d = MemorizingDict()
d.set("boo", 500100) # 1 переменная history = deque(maxlen=10) является атрибутом класса, и доступна и как MemorizingDict.history и как: d = MemorizingDict() d.history
print(d.get_history())


d1 = MemorizingDict()
d1.set("baz", 100500)  # 2 переменная self.history создаётся в момент инициализации объекта, а значит принадлежит объекту и доступна только как: d1 = MemorizingDict() d1.history
print(d1.get_history())
