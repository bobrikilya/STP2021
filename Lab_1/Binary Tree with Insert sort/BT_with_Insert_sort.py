class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.arr = []

    def insertion_sort(self):
        array = self.arr
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()
        self.arr.append(self.data)
        return self.arr


root = Node(12)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
# print(root.print_tree())
# root.insertion_sort()



