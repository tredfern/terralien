import pygsty

_current_turn = 1
_log_to_logger = True
history = []

def last_event():
    if history:
        return history[-1]
    return None

def reset_turn_counter():
    global _current_turn
    _current_turn = 1

def next_turn():
    global _current_turn
    _current_turn += 1


class Entry():
    def __init__(self, message, created_by = None):
        self.message = message
        self.created_at = GameDate()
        self.created_by = created_by
        if _log_to_logger:
            pygsty.logger.info(self.formatted_message())
        global history
        history.append (self)

    def formatted_message(self):
        if self.created_by:
            return "{} {} on {}".format(self.created_by.name, self.message, self.created_at)

class GameDate():
    def __init__(self):
        self.turn = _current_turn

    def __repr__(self):
        return "{}".format(self.turn)
