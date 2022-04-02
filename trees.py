class Node:

    __slots__ = ['_elements']
    
    def __init__(self, val, *children):
        self._elements = [val] + list(children)

    @property
    def children(self):
        return self._elements[1:]

    @children.setter
    def children(self, lst):
        self._elements = self._elements[:1] + list(lst)

    @children.deleter
    def children(self):
        self._elements = self._elements[:1]

    @property
    def value(self):
        return self._elements[0]

    def __repr__(self):
        return "<{}: {} :: {} child nodes>".format(
            self.__class__.__name__, self.value, len(self.children))

    def __iter__(self):
        yield self
        for child in self.children:
            yield from child

    def values(self):
        for node in self:
            yield node.value

"""
     1
    /  \
   2    4
    \   /\
     3  5 6
"""
rootNode = Node(1,Node(2, Node(3)),Node(4, Node(5), Node(6)))

for node in rootNode:
    print(node)

for value in rootNode.values():
    print(value)