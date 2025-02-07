class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        set_ = set()

        node = p
        while node:
            set_.add(node)
            node = node.parent

        node = q
        while node:
            if node in set_:
                return node
            node = node.parent
