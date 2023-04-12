def Node():
	return {'end_of_word':False}

class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self, word):
		node = self.root
		
		for i in range(len(word)):			
			if (word[i] in node) == False:
				node[word[i]] = Node()
		
			if i == len(word)-1 and node[word[i]]['end_of_word'] == False:
				node[word[i]]['end_of_word'] = True
		
			node = node[word[i]]

	def search(self, word):
		node = self.root

		for i in range(len(word)):
			if (word[i] in node) == False:
				return False

			if i == len(word)-1 and node[word[i]]['end_of_word'] == True:
				return True

			node = node[word[i]]

		return False

	def delete(self, word):
		node = self.root

		for i in range(len(word)):
			if (word[i] in node) == False:
				return False

			if i == len(word)-1 and node[word[i]]['end_of_word'] == True:
				node[word[i]]['end_of_word'] = False

			node = node[word[i]]

		return False


trie = Trie()
trie.insert('app')
trie.insert('apple')
trie.insert('apply')
# trie.insert('b')
# trie.insert('c')
# trie.insert('d')
# trie.insert('e')

print(trie.search('apple'))

# import json
# print(json.dumps(trie.root))