class Node:
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.next = None


class HashMap:
	def __init__(self, size):
		self.array = [None] * size		
		self.used_slots = 0
		self.load_factor_threshold = 0.6
	
	def insert(self, key, value):

		bucket_index = self.hashFunction(key, len(self.array))
		
		if self.array[bucket_index] is None:
			self.array[bucket_index] = Node(key, value)
			self.used_slots += 1

		elif self.array[bucket_index].key == key:
			self.array[bucket_index].value = value

		else:
			node = self.array[bucket_index]
			while node.next:
				node = node.next

			node.next = Node(key, value)

		
		load_factor = self.used_slots / len(self.array)

		if load_factor > self.load_factor_threshold:
			self.reHash(key)
			

		
	def get(self, key):
		bucket_index = self.hashFunction(key, len(self.array))
		if self.array[bucket_index] is None:
			return None
		
		elif self.array[bucket_index].key == key:
			# print('key direct match')
			return self.array[bucket_index].value
		else:
			#print('stored in linked list')
			node = self.array[bucket_index]
			while node:
				#print('key: ', node.key)
				if node.key == key:
					return node.value					
				node = node.next
			
			return None

	def remove(self, key):
		bucket_index = self.hashFunction(key, len(self.array))

		if self.array[bucket_index] is None:
			return False
		elif self.array[bucket_index].key == key and self.array[bucket_index].next is None:
			self.array[bucket_index] = None
			return True
		else:
			node = self.array[bucket_index]

			while node:
				if node.key == key:
					prev.next = node.next
					return True
				prev = node
				node = node.next
			return False

	def hashFunction(self, key, size):		
		hashcode = 0
		for i in key:
			hashcode += ord(i)
		return hashcode % size	
	
	def reHash(self, key):		
		old_array = list(self.array)
		self.array = [None] * (len(self.array) * 2)
		self.used_slots = 0			

		for node in old_array:						
			if node is not None:
				head = node				
				if head.next:
					while head.next:
						self.insert(head.key, head.value)
						head = head.next
				else:
					self.insert(head.key, head.value)
						



	def printMap(self, array):
		result = []
		for i in array:
			if i is not None:
				result.append(i.key)
			else:
				result.append(None)

		return result

	

hashmap = HashMap(10)
hashmap.insert('india', 100)
hashmap.insert('nidia', 500)
hashmap.insert('a', 501)
hashmap.insert('b', 502)
hashmap.insert('c', 503)
hashmap.insert('d', 504)
hashmap.insert('e', 505)
hashmap.insert('f', 506)
hashmap.insert('g', 507)
hashmap.insert('hijk', 508)
hashmap.insert('ihjk', 586)
hashmap.insert('jkih', 411)




print('india:', hashmap.get('ihjk'))

# print('nidia:', hashmap.get('nidia'))

print(hashmap.used_slots)

print('jkih', hashmap.get('jkih'))
print(hashmap.remove('jkih'))
print('jkih', hashmap.get('jkih'))


print('ihjk', hashmap.get('ihjk'))
print(hashmap.remove('ihjk'))
print('ihjk', hashmap.get('ihjk'))


print('hijk', hashmap.get('hijk'))
print(hashmap.remove('hijk'))
print('hijk', hashmap.get('hijk'))

print('f', hashmap.get('f'))
print(hashmap.remove('f'))
print('f', hashmap.get('f'))


#print(hashmap.printMap(hashmap.array))