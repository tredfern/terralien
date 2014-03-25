class Walk():
    def __init__(self, actor, path):
        self.actor = actor
        self.path = path

    def perform_action(self):
        if not self.completed():
            next_spot = self.path.pop(0)
            self.actor.moveTo(next_spot.point.x, next_spot.point.y)

    def completed(self):
        return not len(self.path)
