class Node:
    def __init__(self, data):
        self.data = data
        self.next, self.prev = None, None

class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node 
        else:
            last = self.tail
            last.next = node
            node.prev = last
            self.tail = node 

    def prepend(self, node: Node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            temp.prev = node
            node.next = temp 
            self.head = node

    def delete(self, node: Node):
        current = self.head
        while current:
            if current.data == node.data:
                previous_node, next_node = current.prev, current.next
                if previous_node is None:
                    self.head = next_node
                    break 
                if next_node is None:
                    previous_node.next = None 
                    self.tail = previous_node
                    break 
                previous_node.next = next_node
                next_node.prev = previous_node
                break 
            current = current.next

    def printList(self):
        current = self.head
        empty_list = []
        while current:
            empty_list.append(current.data)
            current = current.next
        print(empty_list)


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.printList()
    dll.append(Node(1))
    dll.append(Node(2))
    dll.prepend(Node(0))
    dll.delete(Node(0))
    dll.printList()
