from Snake import *
from Apple import Apple
import numpy as np
import cv2


class GameManager:
    def __init__(self, size, snake):
        self.size = size
        self.snake = snake
        self.apple = Apple.makeRndApple(size[0], size[1])

    def AppleEaten(self):
        if np.all(self.apple.pos == self.snake.head.cord % self.size):
            return True
        else:
            return False

    def snakeColiding(self):
        current_node = self.snake.head.chld

        for i in range(self.snake.length - 1):
            if np.all(current_node.cord % self.size == self.snake.head.cord % self.size):
                return True
            current_node = current_node.chld

        return False

    def onAppleEaten(self):
        self.apple = Apple.makeRndApple(self.size[0], self.size[1])
        self.snake.onAppleEaten()

    def onFrameUpdate(self):
        if self.AppleEaten():
            self.onAppleEaten()
        self.snake.onFrameUpdate()

    def getFrame(self):
        tile_size = Node.img_size
        img = np.zeros((self.size[1] * tile_size, self.size[0] * tile_size, 3))

        current_node = self.snake.head
        for i in range(self.snake.length):
            type = "normal"
            if bool((np.sum(np.array([current_node == self.snake.head, current_node == self.snake.tail])) - 2) * -1):
                if current_node == self.snake.head:
                    type = "head"

                elif current_node == self.snake.tail:
                    type = "tail"

            x_pos = current_node.cord[0] % self.size[0]
            y_pos = current_node.cord[1] % self.size[1]
            img[y_pos * tile_size: (y_pos + 1) * tile_size, x_pos * tile_size: (x_pos + 1) * tile_size, :] += current_node.toImg(type)

            current_node = current_node.chld

        x_pos = self.apple.pos[0]
        y_pos = self.apple.pos[1]
        img[y_pos * tile_size: (y_pos + 1) * tile_size, x_pos * tile_size: (x_pos + 1) * tile_size, :] += apple()

        return img


class Game:
    @staticmethod
    def play(game_size=(30, 20), difficulty="medium"):
        difficulties = {"easy": 80, "medium": 70, "hard": 60, "insane": 40}

        test_snake = Snake(5, np.array([4, 0]), np.array([1, 0]))
        test_game = GameManager(game_size, test_snake)

        img = test_game.getFrame()
        cv2.imshow("SnakeGame", img)
        cv2.waitKey(0)

        while True:
            img = test_game.getFrame()
            cv2.imshow("SnakeGame", img)
            key = cv2.waitKey(difficulties[difficulty]) & 0xFF
            if key == 119 or key == 82:
                test_snake.onUpButtonPress()

            if key == 97 or key == 81:
                test_snake.onLeftButtonPress()

            if key == 115 or key == 84:
                test_snake.onDownButtonPress()

            if key == 100 or key == 83:
                test_snake.onRightButtonPress()

            if key == 27:
                break

            if test_game.snakeColiding():
                break

            test_game.onFrameUpdate()

        cv2.destroyAllWindows()

        game_over = img
        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(game_over, 'Game Over',
                    (int(game_over.shape[1] / 2) - 90, int(game_over.shape[0] / 2)), font, 1, (0, 0, 255), 2)

        cv2.putText(game_over, 'Score: ' + str(test_game.snake.length * 10),
                    ((int(game_over.shape[1] / 2) - 88, int(game_over.shape[0] / 2) + 20)), font, .5, (0, 0, 255), 1)

        while True:
            cv2.imshow("Game Over", game_over)
            key  = cv2.waitKey(1) & 0xFF
            if key == 27:
                break

        cv2.destroyAllWindows()



