# August 2021
# Copyright Chris Frey
# Original code based on this RBT tutorial: youtube.com/playlist?list=PLUrImIkywykzXCJ8Df-qF-Ohys0Cc-gNU

# TODO:
#   Verify correctness of insert and associated RBT rule verification
#   Implement delete and associated RBT rule verification
#   Implement search

class RBT:
    class _Node:
        def __init__(self, key, value, parent):
            self.l = self.r = None
            self.is_b = False
            self.k = key
            self.v = value
            self.p = parent

    def __init__(self):
        self.root = None
    
    def _insert_rules(self, node):
        # Node is root
        if not node.p:
            node.is_b = True
        # Two consecutive red nodes
        elif not node.p.is_b:
            self._resolve_two_reds(node)

    def _resolve_two_reds(self, node):
        # Node is on right of grandparent and aunt is black or null - rotate
        if node.p == node.p.p.r and (not node.p.p.l or node.p.p.l.is_b):
            # Node is on right of parent - left rotate
            if node == node.p.r:
                self._l_rotate(node.p.p)
                self._rotate_color_swap(node.p)
            # Node is on left of parent - right-left rotate
            else:
                self._r_rotate(node.p)
                self._l_rotate(node.p.p)
                self._rotate_color_swap(node)
        # Node is on left of grandparent and aunt is black or null - rotate
        elif node.p == node.p.p.l and (not node.p.p.r or node.p.p.r.is_b):
            # Node is on left of parent - right rotate
            if node == node.p.l:
                self._r_rotate(node.p.p)
                self._rotate_color_swap(node.p)
            # Node is on right of parent - left-right rotate
            else:
                self._l_rotate(node.p)
                self._r_rotate(node.p.p)
                self._rotate_color_swap(node)
        # Aunt is red - color swap
        else:
            self._color_swap(node.p.p)
            self._insert_rules(node.p.p)

    def _r_rotate(self, node):
        tmp = node.l
        tmp.p = node.p
        
        if tmp.r:
            node.l = tmp.r
            tmp.r.p = node
        
        tmp.r = node
        node.p = tmp

    def _l_rotate(self, node):
        tmp = node.r
        tmp.p = node.p

        if tmp.l:
            node.r = tmp.l
            tmp.l.p = node

        tmp.l = node
        node.p = tmp
    
    def _rotate_color_swap(self, node):
        node.is_b = True
        node.r.is_b = node.l.is_b = False

    def _color_swap(self, node):
        node.is_b = False
        node.l.is_b = node.r.is_b = True

    def insert(self, key, value):
        p = None
        n = self.root

        while n:
            p = n
            n = n.r if n.k < key else n.l

        n = self._Node(key, value, p)
        self._insert_rules(n)
