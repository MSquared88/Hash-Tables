# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        if self.storage[index] == None:
            self.storage[index] = LinkedPair(key,value)

        elif node.next == None:

            #check if node key is equal to key if so reasign value
            if node.key == key:
                node.value = value

            # if not key make new node and asign to next
            else:
                node.next = LinkedPair(key, value)
                return 

        else:
            # iterate through ll checking keys 
            while node.next is not None:

                #reasign value if key is key 
                if node.key == key:
                    node.value = value
                    return 
                
                node = node.next

            if node.key == key:
                node.value = value
                return 
            # if key dosent equal any of the keys in the ll asign new node to end
            node.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] == None or self.storage[index][0] is not key:
            return "Key not found"

        self.storage[index] = None


        


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        node = self.storage[index] 

        if node == None:
            return "Key not found"

        if node.key == key:
            return node.value
        
        if node.next is not None:
            # iterate through ll searching for key
            while node.next is not None:
                if node.key == key:
                    return node.value
                node = node.next
            if node.key == key:
                return node.value

        return "Key not found"

        
        
            


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # double capacity of ht
        self.capacity *= 2

        #grab the old storage and assign to a var
        old_storage = self.storage

        #create new empty storage
        self.storage = [None] * self.capacity 

        # iterate through old storage and insert key values into new storage
        node = None
        for old_item in old_storage:
            node = old_item
            while node is not None:
                self.insert(node.key, node.value)
                node = node.next

        



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    
    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))



    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")