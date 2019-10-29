class Player:

    def __init__(self, position):
        self.position  = position
        self.moves = [self.move_down, self.move_left, self.move_up, self.move_right]

    def move_right(self):

    def move_left(self):

    def move_up(self):

    def move_down(self):


    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position