"""
Chopsticks module.
"""
from typing import List


class Chopsticks:
    """A Game called Chopsticks.

    current_state - the current state of game.
    """
    current_state: 'State'

    def __init__(self, is_p1_turn: bool) -> None:
        """"""
        self.current_state = State(is_p1_turn)

    def get_instructions(self) -> str:
        """Return the instructions of game self."""
        return """
        Each of two players begins with one finger pointed up on each of their
        hands.Player A touches one hand to one of Player B's hands, increasing
        the number of fingers pointing up on Player B's hand by the number on
        Player A's hand. The number pointing up on Player A's hand remains the
        same.If Player B now has five fingers up, that hand becomes dead" or
        unplayable. If the number of fingers should exceed five, subtract five
        from the sum. Now Player B touches one hand to one of Player A's hands,
        and the distribution of fingers proceeds as above, including the
        possibility of a dead" hand.Play repeats steps 2-4 until some player
        has two dead" hands, thus losing."""

    def is_over(self, current_state: 'State') -> bool:
        """Return whether the game under current_state is over.
        """
        value = current_state.value
        if current_state.is_p1_turn:
            if value[0] == value[1] == 0:
                return True
        else:
            if value[2] == value[3] == 0:
                return True
        return False


    def is_winner(self, player: str) -> bool:
        """"Return whether player is the winner of game self."""
        if self.is_over(self.current_state):
            if self.current_state.is_p1_turn:
                return player == 'p2'
            elif not self.current_state.is_p1_turn:
                return player == 'p1'
        return False

    def str_to_move(self, move: str) -> str:
        """Return a integer representaton of move for game self."""
        return move


class State:
    """Represent a state of game."""
    is_p1_turn: bool
    value: List[int]

    def __init__(self, is_p1_turn: bool, )\
            ->None:
        """Initialize a new state.
        >>> State(True, [1,2,1,1])"""
        self.is_p1_turn = is_p1_turn
        self.value = [1, 1, 1, 1]




    def get_possible_moves(self) -> List[str]:
        """Return the possible moves of the state self.# There is no move for a
        dead hand.
        >>> a = State(True, [1,2,1,1])
        >>> a.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        """
        result = ['ll', 'lr', 'rl', 'rr']
        if self.is_p1_turn:
            if self.value[0] == 0:
                result.remove('ll')
                result.remove('lr')
            elif self.value[1] == 0:
                result.remove('rl')
                result.remove('rr')
            elif self.value[2] == 0:
                result.remove('ll')
                result.remove('rl')
            elif self.value[3] == 0:
                result.remove('lr')
                result.remove('rl')
        else:
            if self.value[0] == 0:
                result.remove('rl')
                result.remove('ll')
            elif self.value[1] == 0:
                result.remove('rr')
                result.remove('lr')
            elif self.value[2] == 0:
                result.remove('ll')
                result.remove('lr')
            elif self.value[3] == 0:
                result.remove('rl')
                result.remove('rl')
        result.sort()
        return result

    def is_valid_move(self, move_to_make: str)->bool:
        """Return whether move_to_make is a valid move for the next player.
        >>> a = State(True, [1,2,1,1])
        >>> a.is_valid_move('ll')
        True
        >>> a.is_valid_move('rl')
        True
        """
        return move_to_make in self.get_possible_moves()

    def make_move(self, move_to_make: str)->'State':
        """Return a new state of self given move_to_make.
        >>> a = State(True)
        >>> a.value = [0, 2, 3, 0]
        >>> str(a.make_move('rl'))
        'State(p2, 0-2, 0-0)'
        """
        la, lb, ra, rb = self.value[0], self.value[2], self.value[1], self.value[3]
        if self.is_p1_turn:
            new_value = []
            if move_to_make == 'll':
                new_value.extend([la, ra, la+lb, rb])
            elif move_to_make == 'lr':
                new_value.extend([la, ra, lb, la+rb])
            elif move_to_make == 'rl':
                new_value.extend([la, ra, ra+lb, rb])
            elif move_to_make == 'rr':
                new_value.extend([la, ra, lb, ra+rb])
        else:
            new_value = []
            if move_to_make == 'll':
                new_value.extend([la+lb, ra, lb, rb])
            elif move_to_make == 'lr':
                new_value.extend([la, ra+lb, lb, rb])
            elif move_to_make == 'rl':
                new_value.extend([la+rb, ra, lb, rb])
            elif move_to_make == 'rr':
                new_value.extend([la, ra+rb, lb, rb])
        for i in range(4):
            if new_value[i] >= 5:
                new_value[i] -= 5
        new_state = State(not self.is_p1_turn)
        new_state.value = new_value
        return new_state

    def get_current_player_name(self)->str:
        """Return the string representation of the current player name."""
        if self.is_p1_turn:
            return "p1"
        return "p2"

    def __str__(self)->str:
        return 'State({}, {}-{}, {}-{})'.format(self.get_current_player_name(),
                                                self.value[0], self.value[1], self.value[2],
                                                self.value[3])


