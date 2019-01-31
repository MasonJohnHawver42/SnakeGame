import numpy as np
import cv2
from sprites import *

class Node:

    img_size = 10
    current_id = 0

    def __init__(self, cord, dir, parent):
        self.cord = cord
        self.dir = dir
        self.parent = parent
        self.chld = None
        self.id = Node.current_id
        Node.current_id += 1

    def setCord(self, n_cord):
        self.cord = n_cord

    def setChild(self, n_chld):
        self.chld = n_chld

    def toImg(self, type):
        types = {"head": nodeHead(), "tail": nodeTail(), "normal": node()}
        img = types[type]

        num_turns = int(((np.sum((self.dir + np.array([0, np.abs(self.dir[1])])) * np.array([-90, 90])) % 360) / 90))

        for i in range(num_turns):
            img = np.rot90(img)

        return img.astype(np.uint8)

    def __repr__(self):
        return "({}: ({}, {}), ({}, {}))".format(self.id, self.cord[0], self.cord[1], self.dir[0], self.dir[1])

    @staticmethod
    def createLinkedNodeList(length, starting_pos, dir):
        head = Node(starting_pos, dir, None)
        current_node = head
        for i in range(length - 1):
            new_node = Node(current_node.cord - dir, dir, current_node)
            current_node.setChild(new_node)
            current_node = new_node

        return head, current_node


class Snake:

    up_dir = np.array([0, -1])
    down_dir = np.array([0, 1])
    right_dir = np.array([1, 0])
    left_dir = np.array([-1, 0])

    def __init__(self, length, starting_pos, starting_dir):
        self.head, self.tail = Node.createLinkedNodeList(length, starting_pos, starting_dir)
        self.length = length

    def addNode(self):
        new_node = Node(self.tail.cord - self.tail.dir, self.tail.dir, self.tail)
        self.tail.setChild(new_node)
        self.tail = new_node
        self.length += 1

    def onFrameUpdate(self):
        current_node = self.tail

        for i in range(self.length - 1):

            current_node.cord += current_node.dir
            current_node.dir = current_node.parent.dir

            current_node = current_node.parent

        current_node.cord += current_node.dir

    def onUpButtonPress(self):
        if np.all(self.head.dir == Snake.left_dir) or np.all(self.head.dir == Snake.right_dir):
            self.head.dir = Snake.up_dir

    def onDownButtonPress(self):
        if np.all(self.head.dir == Snake.left_dir) or np.all(self.head.dir == Snake.right_dir):
            self.head.dir = Snake.down_dir

    def onRightButtonPress(self):
        if np.all(self.head.dir == Snake.up_dir) or np.all(self.head.dir == Snake.down_dir):
            self.head.dir = Snake.right_dir

    def onLeftButtonPress(self):
        if np.all(self.head.dir == Snake.up_dir) or np.all(self.head.dir == Snake.down_dir):
            self.head.dir = Snake.left_dir

    def onAppleEaten(self):
        for i in range(2):
            self.addNode()

    def toString(self):
        current_node = self.head
        for i in range(self.length):
            print(current_node)
            current_node = current_node.chld