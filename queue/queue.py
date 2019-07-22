class Queue:
    def __init__(self):
        self.size = 0
        # what data structure should we
        # use to store queue elements?
        self.storage = [] 

    def enqueue(self, item):
        self.storage.append(item)
        self.size += 1
  
    def dequeue(self):
        if self.size > 0:
            item = self.storage[0]
            self.storage = self.storage[1:]
            self.size -= 1
            return item
        else:
            return None 

    def len(self):
        return self.size
