class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        
        
class HashMap:
    def __init__(self, size):
        self.bucket = [None] * size
    
    def trace(self, key):
        
        result = ''
        
        bucket_index = self.hashFunction(key)
        
        if self.bucket[bucket_index] is None:
            return 'empty'
        
        elif self.bucket[bucket_index].key == key and self.bucket[bucket_index].next is None:
            return str(self.bucket[bucket_index].value)
        else:
            node = self.bucket[bucket_index]
            
            while node:
                result = result + str(node.value) + '->'
                node = node.next
            
            result = result + 'None'
        
            return result
    def hashFunction(self, key):
        char_code_sum = 0
        
        for char in key:
            char_code_sum = char_code_sum + ord(char)
    
        return char_code_sum % len(self.bucket)
    
    def insert(self, key, value):
        bucket_index = self.hashFunction(key)
        
        if self.bucket[bucket_index] is None:
            
            print(f"insert(): insert at {bucket_index}th index")
            self.bucket[bucket_index] = Node(key, value)
        
        elif self.bucket[bucket_index].key == key:
            print("insert(): update value")
            self.bucket[bucket_index].value = value
        
        else:
            print("insert(): insert new node at the end of the linked list")
            node = self.bucket[bucket_index]
            
            while node.next:
                node = node.next
                
            node.next = Node(key, value)
        
        return True
            
    def get(self, key):
        bucket_index = self.hashFunction(key)
        
        if self.bucket[bucket_index] is None:
            return None
        
        elif self.bucket[bucket_index].key == key:
            print(f"get(): read from {bucket_index}th index")
            return self.bucket[bucket_index].value
        
        else:
            node = self.bucket[bucket_index]
            
            result = None
            
            while node:
                if node.key == key:
                    result = node.value
                    break
                else:
                    node = node.next
            
            
            print("get(): read after traversing the linked list")
            return result
            
    def remove(self, key):
        bucket_index = self.hashFunction(key)
        if self.bucket[bucket_index] is None:
            return None
            
        elif self.bucket[bucket_index].key == key and self.bucket[bucket_index].next is None:
            print("delete():  deleted the single node")
            self.bucket[bucket_index] = None
            return True
        
        elif self.bucket[bucket_index].key == key and self.bucket[bucket_index].next is not None:
            print("delete():  deleted the first node of linked list")
            self.bucket[bucket_index] = self.bucket[bucket_index].next
            return True
        else:
            print("delete():  deleted the middle node of linked list")
            
            node = self.bucket[bucket_index]
            prev = node
            while node:
                
                if node.key == key:
                    prev.next = node.next
                    return True
                
                prev = node
                node = node.next
            
        return False
        
        
   
hm = HashMap(10)
hm.insert('abc', 30)
hm.insert('acb', 40)
hm.insert('cba', 50)
hm.insert('bac', 60)


#print(hm.get('abc'), hm.get('acb'), hm.get('cba'))

print(hm.trace('abc'))
hm.remove('cba')

print(hm.trace('abc'))
hm.remove('bac')
print(hm.trace('abc'))
hm.remove('abc')
print(hm.trace('abc'))
hm.remove('acb')
print(hm.trace('abc'))