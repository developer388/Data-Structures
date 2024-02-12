class Node {
	constructor() {
		this.array = new Array(26).fill(null)
		this.eow = false
	}
}

class Trie {
	constructor() {
		this.root = new Node()
	}

	insert(word) {

		let node = this.root

		for (let i=0; i<word.length; i++) {
			
			const char_index = word[i].charCodeAt() - 'a'.charCodeAt()

			if (node.array[char_index] === null) {				
				node.array[char_index] = new Node()				
			}

			if (i === (word.length-1)) {
				 node.array[char_index].eow = true
			}

			node = node.array[char_index]
		}
	}

	search(word) {
		let node = this.root

		for (let i=0; i<word.length; i++) {
			
			const char_index = word[i].charCodeAt() - 'a'.charCodeAt()

			if (node.array[char_index] === null) {
				return false
			}

			if ( i === (word.length-1) && node.array[char_index].eow === true) {				
				return true			
			}
			node = node.array[char_index]
		}

		return false
	}
}

/*
   {  array : [   ], eow: false}
*/

const trie = new Trie()
trie.insert('ab')

console.log(trie.search('ba'))