class Node {
	constructor(){
		this.dict = {}
		this.eow = false
	}
}


class Trie {
	constructor() {
		this.root = new Node()
	}

	insert(word) {
		let node = this.root

		for (let char of word) {
			if (char in node.dict === false) {
				node.dict[char] = new Node()
			}
			node = node.dict[char]
		}

		node.eow = true
	}

	wordWithPrefix(prefix) {
		let node = this.root, match = ''
		const words = []


		for (let char of prefix) {	
			if (char in node.dict === false) {
				return words
			}
			node = node.dict[char]
		}


		// Once we have traversed to the prefix, we need to traverse all paths that may lead 

		const queue = [{node: node, prefix: prefix}]

		while (queue.length) {
		
			const queue_item = queue.shift()
			const node = queue_item.node
			const prefix = queue_item.prefix

			if (node.eow) {   			// if eow is true push the prefix
 				words.push(prefix)
			}

			for (let char in node.dict) {   // for each key in node.dict push the item to queue
				queue.push({node: node.dict[char], prefix: prefix+char})
			}
		}

        return words
	}

	wordWithPrefixRecursion(prefix) {
		let node = this.root, match = ''
		const words = []


		for (let char of prefix) {	
			if (char in node.dict === false) {
				return words
			}
			node = node.dict[char]
		}


		// Once we have traversed to the prefix, we need to traverse all paths that may lead 


		const recursiveFunction = function (node, prefix, words) {
			if (node.eow) {
				words.push(prefix)
			}

			console.log('prefix:  ', prefix)

			for (let char in node.dict) {   // for each key in node.dict push the item to queue
				recursiveFunction(node.dict[char], prefix+char, words)
			}
		}
		
		// find recursively
		recursiveFunction(node, prefix, words)

        return words
	}
}

const trie = new Trie()
trie.insert('app')
trie.insert('apple')
trie.insert('apply')
trie.insert('appear')

trie.insert('bottle')
trie.insert('bottom')
trie.insert('bot')


console.log(trie.wordWithPrefixRecursion('ap'))

//console.log(JSON.stringify(trie.root, null, 2))