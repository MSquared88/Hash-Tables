# '''
# Linked List hash table key/value pair
# '''

import hashlib
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
        # the operand x << y takes the binary of x and adds y number of 0s to it 
        # and returns what that number is in binary

        hash = 5381
        
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)

        return hash

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity


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
            while node.next is not None and node.key != key:

                node = node.next

            #reasign value if key is key 
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
        node = self.storage[index]
        next_node = None
        while node is not None and node.key != key:
            next_node = node
            node = next_node.next
        if node is None:
            return 'key not found'
        else:
            if next_node is None: 
                self.storage[index] = node.next
            else:
                next_node.next = node.next

            
    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        node = self.storage[index] 

        if node == None:
            return None

        if node.key == key:
            return node.value
        
        if node.next is not None:
            # iterate through ll searching for key
            while node.next is not None and node.key != key:

                node = node.next
            
            if node.key == key:
                return node.value

        return None

        
        
            


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
    ht.insert("line_4", "Linked list saves the day 2!")
    ht.insert("line_5", "Linked list saves the day! 3")
    ht.insert("line_6", "Linked list saves the day! 4")
    ht.insert("line_7", "Linked list saves the day! 5")
    ht.insert("line_8", "Linked list saves the day! 6")

    
    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))


    print(ht.remove("line_3"))
    print(ht.remove("line_5"))
    print(ht.remove("line_8"))

    print("")



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