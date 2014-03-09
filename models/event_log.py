
_current_turn = 1

def reset_turn_counter():
    global _current_turn
    _current_turn = 1

def next_turn():
    global _current_turn
    _current_turn += 1


class Entry():
    def __init__(self, message):
        self.message = message
        self.created_at = GameDate()

class GameDate():
    def __init__(self):
        self.turn = _current_turn
