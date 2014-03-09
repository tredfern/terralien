import pygsty

_current_turn = 1
_log_to_logger = True

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
        if _log_to_logger:
            pygsty.logger.info(self.message)

class GameDate():
    def __init__(self):
        self.turn = _current_turn
