# August 2021
# Copyright Chris Frey
# Original code based on this RBTree tutorial: youtube.com/playlist?list=PLUrImIkywykzXCJ8Df-qF-Ohys0Cc-gNU

# TODO:
#   Implement delete and associated RBTree rule verification
#   Implement search

class RBTree:
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
            print(f'Root, {node.k}, set to black')
        # Two consecutive red nodes
        elif not node.p.is_b:
            print(f'{node.k} and {node.p.k} are both red')
            self._resolve_two_reds(node)

    def _resolve_two_reds(self, node):
        # Node is on right of grandparent and aunt is black or null - rotate
        if node.p == node.p.p.r and (not node.p.p.l or node.p.p.l.is_b):
            print(f'{node.k} aunt is black - rotate')
            # Node is on right of parent - left rotate
            if node == node.p.r:
                print(f'{node.p.k} is right child of {node.p.p.k}\n{node.k} is right child of {node.p.k}')
                self._left_rotate(node.p.p)
                self._rotate_color_correct(node.p)
            # Node is on left of parent - right-left rotate
            else:
                print(f'{node.p.k} is right child of {node.p.p.k}\n{node.k} is left child of {node.p.k}')
                # Passes node parent
                self._right_rotate(node.p)
                # Passes what was node's grandparent before right rotate - now parent
                self._left_rotate(node.p)
                self._rotate_color_correct(node)
        # Node is on left of grandparent and aunt is black or null - rotate
        elif node.p == node.p.p.l and (not node.p.p.r or node.p.p.r.is_b):
            print(f'{node.k} aunt is black - rotate')
            # Node is on left of parent - right rotate
            if node == node.p.l:
                print(f'{node.p.k} is left child of {node.p.p.k}\n{node.k} is left child of {node.p.k}')
                self._right_rotate(node.p.p)
                self._rotate_color_correct(node.p)
            # Node is on right of parent - left-right rotate
            else:
                print(f'{node.p.k} is left child of {node.p.p.k}\n{node.k} is right child of {node.p.k}')
                # Passes node parent
                self._left_rotate(node.p)
                # Passes what was node's grandparent before left rotate - now parent
                self._right_rotate(node.p)
                self._rotate_color_correct(node)
        # Aunt is red - color swap
        else:
            print(f'{node.k} aunt is red - color swap')
            self._color_swap(node.p.p)
            # Recursive call
            self._insert_rules(node.p.p)

    def _right_rotate(self, node):
        tmp = node.l
        node.l = tmp.r
        tmp.r = node

        if node.p:
            if tmp.k < node.p.k:
                node.p.l = tmp
            else:
                node.p.r = tmp

        tmp.p = node.p
        node.p = tmp

        if node.l:    
            node.l.p = node
        
        print(f'Right rotate on: {node.k}')
        print(f'{node.k} parent is now {node.p.k}')

    def _left_rotate(self, node):
        tmp = node.r
        node.r = tmp.l
        tmp.l = node

        if node.p:
            if tmp.k < node.p.k:
                node.p.l = tmp
            else:
                node.p.r = tmp

        tmp.p = node.p
        node.p = tmp

        if node.r:
            node.r.p = node
        
        print(f'Left rotate on: {node.k}')
        print(f'{node.k} parent is now {node.p.k}')
    
    def _rotate_color_correct(self, node):
        print(f'Rotate color correct on: {node.k}')
        print(f'{node.k} is black\n{node.r.k} is red\n{node.l.k} is red')
        node.is_b = True
        node.r.is_b = node.l.is_b = False

    def _color_swap(self, node):
        print(f'Color swap on: {node.k}')
        print(f'{node.k} is red\n{node.r.k} is black\n{node.l.k} is black')
        node.is_b = False
        node.l.is_b = node.r.is_b = True

    def insert(self, key, value):
        parent = None
        node = self.root

        while node:
            parent = node
            node = node.l if key < node.k else node.r

        node = self._Node(key, value, parent)

        if not parent:
            self.root = node
        elif key < parent.k:
            parent.l = node
        else:
            parent.r = node

        if node.p:
            print(f'Inserting: {node.k}\nParent is: {node.p.k}')
        else:
            print(f'Inserting: {self.root.k}\n{self.root.k} is root')

        self._insert_rules(node)

        print('')

rbt = RBTree()
test_nums = [34, 39, 28, 22, 11, 24, 27, 30, 29]

for t_n in test_nums:
    rbt.insert(t_n, None)
