from dashboard import display_cave
import numpy as np


class Node:
    def __init__(self, board):
        self.board = board
        self.children = np.array([])

    def add_child(self, child):
        self.children = np.append(self.children, child)

    def get_children(self):
        return self.children

    def get_board(self):
        return self.board

    def print_tree(self):
        display_cave(self.board)
        for child in self.children:
            child.print_tree()
    def is_leaf(self):
        return len(self.children) == 0
