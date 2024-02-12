class Node:
	def __init__(self):
		self.children = [None] * 26
		self.end_of_word = False

class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self, word):
		
		node = self.root

		for i in range(len(word)):				
			char_ascii_code = ord(word[i])
			char_trie_index = char_ascii_code - ord('a')
	
			if node.children[char_trie_index] is None:
				node.children[char_trie_index] = Node()

			if i == len(word)-1:
				node.children[char_trie_index].end_of_word = True

			node = node.children[char_trie_index]

	def search(self, word):
		node = self.root

		for i in range(len(word)):
			char_ascii_code = ord(word[i])
			char_trie_index = char_ascii_code - ord('a')
			
			if node.children[char_trie_index] is None:
				return False

			if i == len(word)-1 and node.children[char_trie_index].end_of_word == True:
				return True

			node = node.children[char_trie_index]

		return False

	def delete(self, word):
		node = self.root

		for i in range(len(word)):
			char_ascii_code = ord(word[i])
			char_trie_index = char_ascii_code - ord('a')

			if node.children[char_trie_index] is None:
				return False
			
			if i == len(word)-1 and node.children[char_trie_index].end_of_word == True:
				node.children[char_trie_index].end_of_word = False
				return True

			node = node.children[char_trie_index]

		return False

trie = Trie()
# trie.insert('aa')
# trie.insert('aant')
trie.insert('apple')
# trie.insert('apply')

print(trie.root.children[0][0])
# print(trie.search('apple'))
# print(trie.delete('aa'))
# print(trie.search('aa'))