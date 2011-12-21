
class Critter():
  @property
  def habitat(self):
    return self.h

  @property
  def position(self):
    return self.p

  def occupy(self, h):
    self.h = h
    h.add_critter(self)

  def set_position(self, pt):
    if self.h.can_move_to(pt):
      self.p = pt

