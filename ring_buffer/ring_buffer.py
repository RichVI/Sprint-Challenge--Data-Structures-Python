class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        
        # Using Array structure
        self.storage = []
        self.oldest = 0

    def append(self, item):
        # If the length of storage is less than capacity
        if len(self.storage) < self.capacity:
          # Add item into storage
          self.storage.append(item)
        else:
          #Index[0] will be replaced with item
          self.storage[self.oldest] = item

          if self.oldest < len(self.storage) - 1:
            self.oldest += 1
          else:
            self.oldest = 0


    def get(self):
        return self.storage