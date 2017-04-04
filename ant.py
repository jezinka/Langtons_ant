__author__ = 'jezinka'


class Ant:
    position = [0, 0]
    direction = 0
    move_table = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    color = (255, 255, 255, 255)

    def __init__(self, x, y, color):
        self.position = x, y
        self.color = color

    def move(self, clockwise, size):
        self.rotate(clockwise)
        self.add_move(size)
        return self.position

    def add_move(self, size):
        position_x = self.position[0] + self.move_table[self.direction][0]
        position_y = self.position[1] + self.move_table[self.direction][1]

        position_x = 0 if position_x > size[0] - 1 else position_x
        position_x = size[0] - 1 if position_x < 0 else position_x
        position_y = 0 if position_y > size[1] - 1 else position_y
        position_y = size[1] - 1 if position_y < 0 else position_y

        self.position = position_x, position_y

    def rotate(self, clockwise):
        rotate = 1 if clockwise else -1
        self.direction = (self.direction + rotate) % 4
