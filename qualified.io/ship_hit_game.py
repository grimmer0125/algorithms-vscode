# A ship-hit game quesion
def letter_to_coordinate_index(char):
  if char == "A":
    return 0
  elif char == "B":
    return 1
  elif char == "C":
    return 2
  elif char == "D":
    return 3
  elif char == "E":
    return 4
  elif char == "F":
    return 5
  elif char == "G":
    return 6
  elif char == "H":
    return 7
  elif char == "I":
    return 8
  elif char == "J":
    return 9
  elif char == "K":
    return 10
  elif char == "L":
    return 11
  elif char == "M":
    return 12
  elif char == "N":
    return 13
  elif char == "O":
    return 14
  elif char == "P":
    return 15
  elif char == "Q":
    return 16
  elif char == "R":
    return 17
  elif char == "S":
    return 18
  elif char == "T":
    return 19
  elif char == "U":
    return 20
  elif char == "V":
    return 21
  elif char == "W":
    return 22
  elif char == "X":
    return 23
  elif char == "Y":
    return 24
  elif char == "Z":
    return 25

def str_to_coordinate(string):
  # 1B -> [x,y]
  len_ = len(string)
  x = int(string[0: len_-1])-1 # start from 0
  y = letter_to_coordinate_index(string[-1])  # start from 0
  return [x,y]

class ShipObject:
  def __init__(self, ship_str):
    corners = ship_str.split(" ")
    self.top_left = str_to_coordinate(corners[0])
    self.bottom_right = str_to_coordinate(corners[1])
    self.hit_dict = {}
  def test_hit(self, hit):
    x = hit[0]
    y = hit[1]
    if x >= self.top_left[0] and x <= self.bottom_right[0]:
      if y >= self.top_left[1] and y <= self.bottom_right[1]:
        # leave the hit record in self.hit_dict
        key = str(x) + str(y)
        self.hit_dict[key] = 1
        return True

    return False

  def count_hit_dict(self):
    # about hit, 3 kinds
    # not hit
    # hit sunk
    # hit but not sunk,
    # 1. if empty, not hit,
    # if not empty, iterate the 2d array, find in this dict
    # 2 if all found out, means sunk,
    # 3.just hit

    if len(self.hit_dict) == 0:
      return 0,0

    right_x = self.bottom_right[0]+1
    bottom_y = self.bottom_right[1]+1

    # methon2, faster
    if len(self.hit_dict) == (right_x - self.top_left[0]) * (bottom_y-self.top_left[1]):
      return 1,0
    return 0, 1

    # methon1 - iterate 2d array, from [x1, y1] to [x2, y2], slow
    # x_range = range(self.top_left[0], right_x)
    # y_range = range(self.top_left[1], bottom_y)
    # for x in x_range:
    #   for y in y_range:
    #     key = str(x) + str(y)
    #     if key in self.hit_dict:
    #       continue
    #     else:
    #       return 0, 1
    # return 1, 0

# The goal is to count the number of sunk ships and the number of ships that have been hit but not sunk.
def solution(N, S, T):
    if S == "" or T == "":
      return "0,0"

    num_sunk = 0
    num_hit_no_sunk = 0

    # convert S to a array of ShipObject
    ship_array = []
    ship_str_array = S.split(",")
    for ship_str in ship_str_array:
      ship = ShipObject(ship_str)
      ship_array.append(ship)

    # handle T, e.g "2B 2D 3D 4D 4A"
    try_hit_array = T.split(" ")
    for try_hit in try_hit_array:
      hit = str_to_coordinate(try_hit) # [hit_x, hit_y]
      # test each ship
      for ship in ship_array:
        if ship.test_hit(hit):
          break

    # try to count the result
    for ship in ship_array:
      sunk_count, hit_count = ship.count_hit_dict()
      num_sunk += sunk_count
      num_hit_no_sunk += hit_count
    return str(num_sunk)+"," + str(num_hit_no_sunk)

def test_func():
    assert solution(4, "1B 2C,2D 4D", "2B 2D 3D 4D 4A") == "1,1"
    assert solution(3, "1A 1B,2C 2C", "1B") == "0,1"
    assert solution(12, "1A 2A,12A 12A", "12A") == "1,0"
    assert solution(2, '1A 2A', '') == "0,0"
    assert solution(2, '', '2A') == "0,0"
