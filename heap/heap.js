class MinHeap  {
	constructor() {
		this.array = []
	}

	insert(value) {

		this.array.push(value)                        // insert the value at the end of the array

		let index_of_new_node = this.array.length - 1

		//console.log("\n\ninserting ", value)
		while (index_of_new_node > 0) {               // while newly inserted value is not reached to root

			let value_of_new_node = this.array[index_of_new_node]

			let index_of_parent = Math.floor((index_of_new_node-1)/2)
			let value_of_parent = this.array[index_of_parent]

		//	console.log(`i=${value_of_new_node}, p=${value_of_parent}`)


			if (value_of_parent > value) {			 //  swap the child with parent   
				this.array[index_of_parent] = value
				this.array[index_of_new_node] = value_of_parent				
			}
			else {
				break								 //  break from the loop if swap is not required
			}

			index_of_new_node = index_of_parent
		}

		//console.log(this.array)
	}

	remove() {

		//console.log('\n\nremove() from ', this.array)

		if (this.array.length === 0) {
			return null
		}

		if (this.array.length === 1) {
			return this.array.pop()
		}

		const result = this.array[0]

		this.array[0] = this.array.pop()

		let index_of_parent = 0
		
		
		while (index_of_parent < this.array.length) {

			let index_of_left_child = (2 * index_of_parent) + 1
			let value_of_left_child = this.array[index_of_left_child]			
			
			let index_of_right_child = (2 * index_of_parent) + 2
			let value_of_right_child = this.array[index_of_right_child]
        	
        	let index_of_smallest_child = index_of_parent
            

			if (index_of_left_child < this.array.length && value_of_left_child < this.array[index_of_smallest_child]) {
				index_of_smallest_child = index_of_left_child
			}

			if (index_of_right_child < this.array.length && value_of_right_child < this.array[index_of_smallest_child]) {
				index_of_smallest_child = index_of_right_child
			}
			
			if (index_of_smallest_child === index_of_parent) {
				break
			}

			// swap values using destructuring [a, b] = [b, a]
			[this.array[index_of_parent], this.array[index_of_smallest_child]] = [this.array[index_of_smallest_child], this.array[index_of_parent]]
			index_of_parent = index_of_smallest_child
			
		}

		return result
	}


	heapifyDown(index_of_parent, array) {

		let index_of_left_child = (2 * index_of_parent ) + 1
		let index_of_right_child = (2 * index_of_parent ) + 2

		let index_of_smallest_child = index_of_parent

		if (index_of_left_child < array.length && array[index_of_left_child] < array[index_of_smallest_child]){
			index_of_smallest_child = index_of_left_child
		}

		if (index_of_right_child < array.length && array[index_of_right_child] < array[index_of_smallest_child]){
			index_of_smallest_child = index_of_right_child
		}
		
		if (index_of_smallest_child != index_of_parent) {
			[array[index_of_parent], array[index_of_smallest_child]] = [array[index_of_smallest_child], array[index_of_parent]]
			this.heapifyDown(index_of_smallest_child, array)
		}

	}

	convertArrayToHeap(array) {
		let index_of_last_non_leaf_node = Math.floor(array.length/2) - 1

		for (let index_of_parent = index_of_last_non_leaf_node; index_of_parent>=0; index_of_parent--) {
			this.heapifyDown(index_of_parent, array)
			
		}

		return array
	}
}

const heap = new MinHeap()
// heap.insert(9)
// heap.insert(8)
// heap.insert(10)
// heap.insert(29)
// heap.insert(39)
// heap.insert(1)
// heap.insert(2)
// heap.insert(4)
// heap.insert(100)
// heap.insert(0)

// console.log(heap.array)
// console.log("remove(): ",heap.remove())
// console.log("remove(): ",heap.remove())
// console.log("remove(): ",heap.remove())
// console.log("remove(): ",heap.remove())
// console.log("remove(): ",heap.remove())
// console.log("remove(): ",heap.remove())
// console.log("remove(): ",heap.remove())
// console.log("remove(): ",heap.remove())
// console.log("remove(): ",heap.remove())
// console.log("remove(): ",heap.remove())

const array = [9,8,10,29,39,1,2,4,100,0]

console.log(heap.array)

heap.array = heap.convertArrayToHeap(array)


console.log(heap.array)
console.log("remove(): ",heap.remove())
console.log("remove(): ",heap.remove())
console.log("remove(): ",heap.remove())
console.log("remove(): ",heap.remove())
console.log("remove(): ",heap.remove())
console.log("remove(): ",heap.remove())
console.log("remove(): ",heap.remove())
console.log("remove(): ",heap.remove())
console.log("remove(): ",heap.remove())
console.log("remove(): ",heap.remove())