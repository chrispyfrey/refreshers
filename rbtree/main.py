# August 2021
# Copyright Chris Frey
# General structure and insert function based on: youtube.com/playlist?list=PLUrImIkywykzXCJ8Df-qF-Ohys0Cc-gNU
# Remove function is original, but is likely not novel

# TODO:
#   Implement remove node:
#       Handle first-child null from in-order functions
#       Implement remove black node
#   Test/verify correctness of node removal

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
        self.size = 0
    
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

    def _get_node(self, key):
        # Non-empty tree
        if self.root:
            node = self.root

            while node.k != key:
                node = node.l if key < node.k else node.r
                
                # Key not in tree
                if not node: 
                    return None
            # Key found
            return node
        # Empty tree
        else:
            return None
    
    def _nord_predecessor(self, node):
        n = node.l
        depth = 0
        
        if n:
            depth += 1
            while n.r:
                n = n.r
                depth += 1

        return (n, depth)

    def _nord_successor(self, node):
        n = node.r
        depth = 0

        if n:
            depth += 1
            while n.l:
                n = n.l
                depth += 1

        return (n, depth)

    def _replace_node(self, old_n, new_n):
        new_n.p = old_n.p
        new_n.l = old_n.l
        new_n.r = old_n.r
        new_n.is_b = old_n.is_b

        # Old node is not root
        if old_n.p:
            if old_n.p.l == old_n:
                old_n.p.l = new_n
            else:
                old_n.p.r = new_n

    def _remove_red(self, node):
        if node.p.l == node:
            node.p.l = None
        else:
            node.p.r = None

    def _remove_black(self, node):
        if node.l:
            node.l = None
            self._replace_node(node, node.l)
        elif node.r:
            node.r = None
            self._replace_node(node, node.r)
        else:
            pass

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
        self.size += 1

        print('')

    # Removes target node and replaces with either the in-order predecessor or successor
    # Chooses more populated side of node
    def remove(self, key):
        node = self._get_node(key)

        # Tree is not empty
        if node:
            # Get in-order calls could be run in parallell
            pred, pred_dpth = self._nord_predecessor(node)
            scsr, scsr_dpth = self._nord_successor(node)

            # Depths are the same relative to node
            if pred_dpth == scsr_dpth:
                # Both are black
                if pred.is_b and scsr.is_b:
                    # Both are leaves OR successor is not a leaf - choose successor (arbitrary for both non-leaves)
                    if (pred.l == pred.r and scsr.l == scsr.r) or scsr.r:
                        self._remove_black(scsr)
                        self._replace_node(node, scsr)
                    # Predecessor is not a leaf and successor is a leaf - choose predecessor
                    else:
                        self._remove_black(pred)
                        self._replace_node(node, pred)
                # Predecessor is black, sucessor is red - choose predecessor
                elif pred.is_b:
                    self._remove_black(pred)
                    self._replace_node(node, pred)
                # Predecessor is red, successor is black - choose successor
                elif scsr.is_b:
                    self._remove_black(scsr)
                    self._replace_node(node, scsr)
                # Both are red - arbitrarily choose successor
                else:
                    self._remove_red(scsr)
                    self._replace_node(node, scsr)
            # Predecessor is further from node than successor - choose predecessor
            elif pred_dpth > scsr_dpth:
                self._remove_black(pred) if pred.is_b else self._remove_red(pred)
                self._replace_node(node, pred)
            # Successor is further from node than predecessor - choose sucessor
            else:
                self._remove_black(scsr) if scsr.is_b else self._remove_red(scsr)
                self._replace_node(node, scsr)

            self.size -= 1
            return node.v

        return None

    def get(self, key):
        # Non-empty tree
        if self.root:
            node = self.root

            while node.k != key:
                node = node.l if key < node.k else node.r
                # Key not in tree
                if not node: 
                    return None
            # Key found
            return node.v
        # Empty tree
        else:
            return None

    def size(self):
        return self.size

rbt = RBTree()
test_nums = [34, 39, 28, 22, 11, 24, 27, 30, 29]

for t_n in test_nums:
    rbt.insert(t_n, None)
