class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList():
    def __init__(self):
        self.head = None

    def append(self, node: Node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def prepend(self, node: Node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head 
            node.next = temp
            self.head = node 

    def delete(self, node: Node):
        current = self.head
        previous_node = None
        while current:
            if current.data == node.data:
                next_node = current.next
                if previous_node is None:
                    self.head = next_node
                else:
                    previous_node.next = next_node
                break
            previous_node = current
            current = current.next


    def printList(self):
        current = self.head
        empty_list = []
        while current:
            empty_list.append(current.data)
            current = current.next
        print(empty_list)


if __name__ == "__main__":
    dll = SinglyLinkedList()
    dll.printList()
    dll.append(Node(1))
    dll.append(Node(2))
    dll.prepend(Node(0))
    dll.delete(Node(1))
    dll.printList()
