import node
from node import Node
from node import Color


class RedBlackTree:
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def search(self, word):
        return self._search_in_RBT(word, self.__root)

    def _search_in_RBT(self, word, node):
        if node is None:
            return None
        if node.get_value() == word:
            return node
        elif node.get_value() > word:
            return self._search_in_RBT(word, node.get_leftChild())
        elif node.get_value() < word:
            return self._search_in_RBT(word, node.get_rightChild())

    def print_Black_height(self):
        print("Black height in RBT is ", self._calculate_Black_height(self.__root))

    def _calculate_Black_height(self, node):
        if node is None:
            return 0
        if node.get_color() == Color.BLACK:
            return 1 + self._calculate_Black_height(node.get_leftChild())
        else:
            return self._calculate_Black_height(node.get_leftChild())

    def print_Tree_height(self):
        print("Tree height is ", self._calculate_Tree_height(self.__root))

    def _calculate_Tree_height(self, node):
        if node is None:
            return 0  # can also be -1 --> check
        left_height = self._calculate_Tree_height(node.get_leftChild())
        right_height = self._calculate_Tree_height(node.get_rightChild())
        return max(left_height, right_height) + 1

    def print_Tree_size(self):
        print("Tree Size is = ", self.calculate_RBT_size(self.__root))

    def calculate_RBT_size(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.calculate_RBT_size(node.get_leftChild()) + self.calculate_RBT_size(node.get_rightChild())

    def insert(self, value):
        new_node = Node(value)
        self.insert_in_tree(new_node)

    def getCurrentNode(self, current_node, value):
        if current_node is None:
            return current_node
        if value < current_node.get_value():
            return self.getCurrentNode(current_node.get_leftChild(), value)
        else:
            return self.getCurrentNode(current_node.get_rightChild(), value)

    def get_uncle(self, p, gp):
        if gp is None:
            return None
        if gp.get_leftChild() is p:
            return gp.get_rightChild()
        else:
            return gp.get_leftChild()

    def recolor(self, node):
        if node.get_color() == Color.RED:
            node.set_color(Color.BLACK)
        else:
            node.set_color(Color.RED)

    def rotate_left(self, node):
        node_right = node.get_rightChild()
        node.set_rightChild(node_right.get_leftChild())

        if node.get_rightChild() is not None:
            node.get_rightChild().set_parent(node)

        if node.get_parent() is None:
            self.__root = node_right
            node_right.set_parent(None)
        else:
            node_right.set_parent(node.get_parent())
            if node.get_parent().get_rightChild() == node:
                node_right.get_parent().set_rightChild(node_right)
            else:
                node_right.get_parent().set_leftChild(node_right)

        node_right.set_leftChild(node)
        node.set_parent(node_right)

    def rotate_right(self, node):
        node_left = node.get_leftChild()
        node.set_leftChild(node_left.get_rightChild())

        if node.get_leftChild() is not None:
            node.get_leftChild().set_parent(node)

        if node.get_parent() is None:
            self.__root = node_left
            node_left.set_parent(None)
        else:
            node_left.set_parent(node.get_parent())
            if node.get_parent().get_rightChild() == node:
                node_left.get_parent().set_rightChild(node_left)
            else:
                node_left.get_parent().set_leftChild(node_left)
        node_left.set_rightChild(node)
        node.set_parent(node_left)

    def fix_Insertion(self, node):
        if node.get_parent() is None:
            node.set_color(Color.BLACK)
            return
        p = node.get_parent()
        gp = p.get_parent()
        if gp is not None:
            if p.get_color() == Color.RED:
                u = self.get_uncle(p, gp)
                if u is not None and u.get_color() == Color.RED:
                    self.recolor(p)
                    self.recolor(gp)
                    self.recolor(u)
                    self.fix_Insertion(gp)
                elif u is None or u.get_color() == Color.BLACK:
                    # left, left
                    if p.get_leftChild() is node and gp.get_leftChild() is p:
                        self.recolor(gp)
                        self.recolor(p)
                        self.rotate_right(gp)

                    # left, right
                    elif p.get_rightChild() is node and gp.get_leftChild() is p:
                        self.recolor(gp)
                        self.recolor(node)
                        self.rotate_left(p)
                        self.rotate_right(gp)


                    # right, right
                    elif p.get_rightChild() is node and gp.get_rightChild() is p:
                        self.recolor(gp)
                        self.recolor(p)
                        self.rotate_left(gp)

                    # right, left
                    elif p.get_leftChild() is node and gp.get_rightChild() is p:
                        self.recolor(gp)
                        self.recolor(node)
                        self.rotate_right(p)
                        self.rotate_left(gp)

    def insert_in_tree(self, new_node):
        if self.__root is None:
            self.__root = new_node
            self.__root.set_color(node.Color.BLACK)
            return
        parent_node = None
        current_node = self.__root
        while current_node is not None:
            parent_node = current_node
            if new_node.get_value() < current_node.get_value():
                current_node = current_node.get_leftChild()
            else:
                current_node = current_node.get_rightChild()

        # Assign the parent to the new_node
        new_node.set_parent(parent_node)

        # Insert the new_node as the left or right child
        if new_node.get_value() < parent_node.get_value():
            parent_node.set_leftChild(new_node)
        else:
            parent_node.set_rightChild(new_node)

        self.fix_Insertion(new_node)

    def inorder_traversal_to_file(self, node, file):
        if node is not None:
            self.inorder_traversal_to_file(node.get_leftChild(), file)
            file.write(str(node.get_value()) + "\n")  # Write the key of the current node to the file
            self.inorder_traversal_to_file(node.get_rightChild(), file)
