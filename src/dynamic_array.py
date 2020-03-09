class DynamicArray: 
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    def insert(self, index, value):
        if self.count >= self.capacity:
            self.double_size()

        #index in range    
        if index > self.count:
            print("ERROR: Index out of range")
            return
        
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i-1]

        #insert
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)
    
    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]
        self.storage = new_storage

my_arr = DynamicArray(4)

my_arr.insert(0, 1)
my_arr.insert(0, 2)
my_arr.insert(1, 3)
my_arr.insert(3, 4)
my_arr.append(20)


print(my_arr.storage)



