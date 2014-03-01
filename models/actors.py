
class Actor():
    def __init__(self, position=(0,0)):
        self.position = position

    @property
    def x(self):
        return self.position[0]

    @property
    def y(self):
        return self.position[1]
