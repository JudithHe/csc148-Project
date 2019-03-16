"""
SubtractSqaure module.
"""
from typing import List
from math import sqrt


class SubtractSquare:
    """A Game called SubtractSqaure.

    current_state - the current state of game.
    """
    current_state: 'State'

    def __init__(self, is_p1_turn: bool)->None:
        """Initialize a new game SubtractSquare."""
        num = int(input('type in a non-negative number:'))
        self.current_state = State(is_p1_turn, num)

    def get_instructions(self)->str:
        """Return the instructions of game self."""
        return """
        A non-negative whole number is chosen as the starting value by some 
        neutral entity.The player whose turn it is chooses some square of a 
        positive whole number (such as 1, 4, 9, 16, . . . )to subtract from the 
        value, provided the chosen square is not larger. After subtracting, we 
        have a new value and the next player chooses a square to 
        subtract from it.
        """

    def is_over(self, current_state:'State')->bool:
        """Return whether the game is over under the current_state."""
        return current_state.num == 0  # can use len of get_possile_move

    def is_winner(self, player: str)->bool:
        """Return whether player is the winner of game self."""
        if self.is_over(self.current_state):
            return self.current_state.get_current_player_name() != player
            # .get_current_player_name()==player indi p is loser.
        return False

    def str_to_move(self, move: str)-> int:
        """Return a integer representaton of move for game self.
        >>> a = SubtractSquare()
        >>> a.str_to_move('10')
        10
        """
        return int(move)

    def __str__(self)->str:
        """Return a string representation of self.
        """
        return 'current value is {}'.format(self.current_state.num)

    def __eq__(self, other: 'SubtractSquare')->bool:
        """Return whether self is equivalent to other."""
        return type(self) == type(other) and self.current_state == other.\
            current_state


class State:
    """Represent a state of game."""
    is_p1_turn: bool
    num: int

    def __init__(self, is_p1_turn: bool, num: int)->None:
        """Initialize a new state."""
        self.is_p1_turn = is_p1_turn
        self.num = num

    def get_possible_moves(self) -> List[int]:
        """Return the possible moves of the state self.
        >>> a = State(True, 16)
        >>> a.get_possible_moves()
        [1, 4, 9, 16]
        """
        root = int(sqrt(self.num))
        return [i**2 for i in range(1, root+1)]

    def is_valid_move(self, move_to_make: int)->bool:
        """Return whether move_to_make is a valid move of state self.
        >>> a = State(True, 16)
        >>> a.is_valid_move(4)
        True
        """
        return move_to_make in self.get_possible_moves()

    def make_move(self, move_to_make: int)->'State':
        """Return a new state of self given move_to_make."""
        # if self.is_p1_turn:
        #     player = False
        # else:
        #     player = True
        player = not self.is_p1_turn
        num = self.num - move_to_make
        return State(player, num)

    def get_current_player_name(self)->str:
        """Return the string representation of the current player name."""
        if self.is_p1_turn:
            return "p1"
        return "p2"

    def __str__(self)->str:
        return 'The current player is {} and the current value is {}'.\
            format(self.get_current_player_name(), self.num)

    def __eq__(self, other: 'State')->bool:
        """Return whether self is equivalent to other."""
        return type(self) == type(other) and self.is_p1_turn == other.\
            is_p1_turn and self.num == other.num


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config="a1_pyta.txt")
