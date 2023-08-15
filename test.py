lines = """
He took his vorpal sword in hand;
      Long time the manxome foe he sought—
So rested he by the Tumtum tree
      And stood awhile in thought.
"""

line_list = lines.splitlines()
print(' "the" in line_list[0] --> ' + str(bool("the" in line_list[0])))
print(' "the" in line_list[1] --> ' + str(bool("the" in line_list[1])))
print('0 + False + True = ' + str(0 + False + True))   # [Equivalent to 0 + 0 + 1]
# print(bool(["the" in line for line in line_list]))   # [Phải ra: <False, True, True, False> nma chạy chỉ ra <True>]    ???
print('False + True + True + False = ' + str(False + True + True + False))