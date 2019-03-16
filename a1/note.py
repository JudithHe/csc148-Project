class State:
    is_p1_turn: bool
    l1: int
    r2: int


    def __init__(self, is_p1_turn: bool, l1: int, r1: int, l2:int, r2:int)->None:
        """Initialize a new state."""
        self.is_p1_turn = is_p1_turn
        self.l1 = l1
        self.r1 = r1
        self.l2 = l2
        self.r2 = r2

    def make_move(self, move_to_make: tuple) -> 'State':
        """
        >>> a = State(True, 0, 2, 1, 0)
        >>> a.make_move(('left', 1))
        State(False, 0, 2, 2, 0)
        """
        if self.is_p1_turn:
            if move_to_make[0] == "right":
                right_sum = self.r2 + move_to_make[1]
            else:
                left_sum = self.l2 + move_to_make[1]
            return State(not self.is_p1_turn, self.l1, self.r1, left_sum, right_sum)
        elif not self.is_p1_turn:
            if move_to_make[0] == "right":
                right_sum = self.r1 + move_to_make[1]
            else:
                left_sum = self.l1 + move_to_make[1]
            return State(not self.is_p1_turn, left_sum, right_sum, self.l2,
                         self.r2)

a = State(True, 0, 2, 1, 0)
print(a.make_move(('left', 1)))
