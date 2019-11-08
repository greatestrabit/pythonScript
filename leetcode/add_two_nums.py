class LinkedNode:
    def __init__(self):
        self.val = None
        self.next = None
        self.depth = 0

    def link(self, data):
        self.depth = self.depth + 1
        if self.val is not None:
            node = LinkedNode()
            node.val = data
            self.next = node
            return node
        else:
            self.val = data
            return self

    @staticmethod
    def print_link(node):
        while node:
            if node.next:
                print(str(node.val) + '->', end='')
            else:
                print(str(node.val))
            node = node.next

    @staticmethod
    def depth(node):
        depth = 0
        while node:
            if node.val:
                depth = depth + 1
            node = node.next
        return depth


def addTwoNumbers(l1: list, l2: list):
    node1 = LinkedNode()
    node = node1
    for data in l1:
        node = node.link(data)
    LinkedNode.print_link(node1)

    node2 = LinkedNode()
    node = node2
    for data in l2:
        node = node.link(data)
    LinkedNode.print_link(node2)

    result_node = LinkedNode()
    temp_node = result_node
    if LinkedNode.depth(node1) >= LinkedNode.depth(node2):
        addition = 0
        while node1:
            if node2 and node2.val:
                result = node1.val + node2.val
                node2 = node2.next
            else:
                result = node1.val

            temp_node = temp_node.link((result + addition) % 10)
            addition = (result + addition) // 10
            node1 = node1.next
        if addition > 0:
            temp_node = temp_node.link(addition)

    LinkedNode.print_link(result_node)


addTwoNumbers([1, 8, 3, 4], [1, 8, 7, 6])
