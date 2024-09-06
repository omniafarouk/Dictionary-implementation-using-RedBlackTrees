from redblacktree import RedBlackTree


def check_insertions(tree):
    tree.print_Black_height()
    tree.print_Tree_height()
    tree.print_Tree_size()


class File:

    @staticmethod
    def readfile(filename, tree):
        with open(filename, 'r') as file:
            for line in file:
                value = line.strip()
                tree.insert(value)
                # check_insertions(tree)
                # insert as a node in redblack tree

    @staticmethod
    def write_to_file(filename, tree):
        with open(filename, "w") as file:
            tree.inorder_traversal_to_file(tree.get_root(), file)


class Dictionary:

    def __init__(self, filename):
        self.tree = RedBlackTree()
        # check_insertions(self.tree)
        self.load(filename)


    def insert(self):
        new_word = input("Enter a word to insert in file: ")
        found = self.tree.search(new_word)
        if found is not None:
            print("“ERROR: Word already in the dictionary!")
        else:
            self.tree.insert(new_word)
            print("word added to file successfully!")
            check_insertions(self.tree)
            # insert in tree

    def Look_up(self):
        word = input("Enter a word to search: ")
        found = self.tree.search(word)
        if found is None:
            print("NO")
            print("Word is not in dictionary!")
        else:
            print("YES")
            print("Word is in dictionary!")

    def load(self, filename):
        File.readfile(filename, self.tree)
        check_insertions(self.tree)

    def save_to_file(self, filename):
        File.write_to_file(filename, self.tree)
