"""
Game module.
"""


class Game:
    """Represent a game of a restricted type, namely two-player, sequential-move,
    zero-sum, perfect-information.

    current_state - the current state of game.
    """
    current_state: 'State'

    def __init__(self, is_p1_turn: bool)->None:
        """"""
        raise NotImplementedError('Subclasss is needed!')

    def get_instructions(self)->str:
        """"""
        raise NotImplementedError('Subclasss is needed!')

    def is_over(self, current_state: 'State')->bool:
        """"""
        raise NotImplementedError('Subclasss is needed!')

    def is_winner(self, player: str)->bool:
        """"""
        raise NotImplementedError('Subclasss is needed!')

    def str_to_move(self, move):
        """"""
        raise NotImplementedError('Subclasss is needed!')


class State:

    def __init__(self)->None:
        """"""
        raise NotImplementedError('Subclasss is needed!')

    def get_possible_moves(self) -> list:
        """"""
        raise NotImplementedError('Subclasss is needed!')

    def is_valid_move(self, move_to_make)->bool:
        """"""
        raise NotImplementedError('Subclasss is needed!')

    def make_move(self, move_to_make)->'State':
        """"""
        raise NotImplementedError('Subclasss is needed!')

    def get_current_player_name(self)->str:
        """"""
        raise NotImplementedError('Subclasss is needed!')

    def __str__(self)->str:
        """"""
        raise NotImplementedError('Subclasss is needed!')
