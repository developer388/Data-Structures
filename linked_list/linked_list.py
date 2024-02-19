class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):

        if self.head is None:
            print('empty')
        else:
            node = self.head

            result = ''
            while node:
                result = result + str(node.value) + '->'
                node = node.next

            result = result + 'None'
            print(result)

    def insertAtTail(self, value):

        if self.head is None:
            self.head = Node(value)
        else:

            node = self.head

            while node.next:
                node = node.next

            node.next = Node(value)

        return True

    def findThenDelete(self, value):

        if self.head is None:                                           # linked list is empty
            return False
        elif self.head.value == value and self.head.next is None:       # linked list has only one node
            self.head = None
            return True
        elif self.head.value == value and self.head.next is not None:   # first node needs to be deleted, update the head
            self.head = self.head.next
            return True
        else:                                                           # middle node needs to be deleted, traverse
            node = self.head
            prev = node

            while node:

                if node.value == value:
                    prev.next = node.next
                    return True

                prev = node
                node = node.next

            return False

    def readFromIndex(self, index):
        counter = 0

        if self.head is None:
            return None
        else:
            node = self.head

            while node:
                if counter == index:
                    return node.value

                node = node.next
                counter = counter + 1
        return None

    def insertAtIndex(self, index, value):
    
        if index == 0 :
            if self.head is None:
                self.head = Node(value)
            else:
                node = Node(value)
                node.next = self.head
                self.head = node
            return True
        else:
            counter = 0
            node = self.head            
            prev = node
            while node:
                if counter == index:
                    new_node = Node(value)
                    prev.next = new_node
                    new_node.next = node.next
                    return True

                prev = node
                node = node.next
                counter = counter + 1
        return False

    def updateAtIndex(self, index, value):

        counter = 0

        node = self.head

        while node:

            if counter == index:
                node.value = value
                return True

            node = node.next
            counter = counter + 1

        return False

    def deleteFromIndex(self, index):

        if self.head is None:
            False

        if index == 0:
            self.head = self.head.next
            return True

        else:
            counter = 0

            node = self.head
            prev = node
            
            while node:

                if counter == index:
                    prev.next = node.next
                    return True

                prev = node
                node = node.next
                counter = counter + 1

        return False



ll = LinkedList()

ll.insertAtTail(1)
ll.insertAtTail(2)
# ll.insertAtTail(3)
# ll.insertAtTail(4)
# ll.insertAtTail(5)
# ll.insertAtTail(6)

ll.print()

# print(ll.insertAtIndex(0, 0))

# print(ll.insertAtIndex(1, 31))
# ll.print()

# print(ll.insertAtIndex(7, 31))

# ll.print()

# print(ll.updateAtIndex(6, 100))
# ll.print()

print(ll.deleteFromIndex(1))
ll.print()