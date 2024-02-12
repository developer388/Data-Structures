class Heap {


    heap = []


    constructor(array) {

        if (array && array.length) {
            for (var i in array) {
                this.insert(array[i])
            }
        }
    }
    insert(value) {
        this.heap.push(value) // add element at leaf
        var value_index = this.heap.length - 1 // set index of element
        while (value_index > 0) { // iterate till we reach root node
            var parent_index =
                Math.floor((value_index - 1) / 2) // set index of parent node
            var parent_value = this.heap[parent_index] // set value of parent node
            if (value < parent_value) { // if value of current element is greater than parent node; tweak for min/max heap
                this.heap[value_index] = parent_value // replace value of current node with parent
                this.heap[parent_index] = value // replace value of parent node with current node
            } else { // if value of current element is less than parent node, exit from loop. heap property is reserved
                break
            }
            value_index = parent_index // set value_index as parent, parent to be checked and adjusted in next iteration

        }
    }
    delete() {
        if (this.heap.length < 1) {
            console.log('deletion: empty heap !')
            return false
        }
        if (this.heap.length === 1) {
            return this.heap.pop()
        }
        var index = 0,
            value,
            left_child_index,
            right_child_index,
            swap_index = 0,
            pop_element = this.heap[index]
        this.heap[index] = this.heap.splice(this.heap.length -1, 1)[0] // replace value of root node with value of last leaf node, remove leaf node
        value = this.heap[index]
        while (true) {
            left_child_index = Math.floor((2 * index) + 1)
            right_child_index = Math.floor((2 * index) + 2)
            if (left_child_index < this.heap.length && this.heap[left_child_index] < this.heap[index]) { // tweak for min/max heap
                swap_index = left_child_index
            }
            if (right_child_index < this.heap.length && this.heap[right_child_index] < this.heap[index]) { // tweak for min/max heap
                swap_index = right_child_index
            }
            if (swap_index < index) { // tweak for min/max heap
                this.heap[index] = this.heap[swap_index]
                this.heap[swap_index] = value
            } else {
                break
            }
            index = swap_index
        }
        return pop_element
    }
}
// module.exports = Heap
heap = new Heap([])


heap.insert(9)
heap.insert(8)
heap.insert(10)
heap.insert(29)
heap.insert(39)
heap.insert(1)
heap.insert(2)
heap.insert(4)
heap.insert(100)

console.log("heap:",heap.heap)

// for (let i=0; i<heap.heap.length; i++) {
//     console.log(`i=${heap.heap[i]} l:${heap.heap[(i*2)+1]}, r: ${heap.heap[(i*2)+2]}`)
// }



console.log("remove(): ",heap.delete())

console.log("heap:",heap.heap)

console.log("delete(): ",heap.delete())
console.log("heap:",heap.heap)

// console.log("delete(): ",heap.delete())
// console.log("delete(): ",heap.delete())
// console.log("delete(): ",heap.delete())
// console.log("delete(): ",heap.delete())