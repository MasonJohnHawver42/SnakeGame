import numpy as np


def nodeHead():
    node_head = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                          [0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
                          [0, 0, 1, 0, 1, 1, 0, 1, 0, 0],
                          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    node_head = (node_head * 255).repeat(3).reshape((10, 10, 3))
    return node_head


def node():
    node = np.zeros((10, 10, 3))
    node[1: 9, 1: 9, :] = 255
    return node


def nodeTail():
    node_tail = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                          [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                          [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

    node_tail = (node_tail * 255).repeat(3).reshape((10, 10, 3))
    return node_tail


def apple():
    apple = np.zeros((10, 10, 3))
    apple[3: 7, 3: 7, :] = 255
    apple[:, :, [0, 1]] = 0
    return apple

