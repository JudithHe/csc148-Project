"""Game Stonehenge"""
from typing import List, Any
from game import Game
from game_state import GameState


class StonehengeGame(Game):
    """Create a new game called StonehengeGame.
     A subclass of class Game."""
    current_state: 'StonehengeState'

    def __init__(self, p1_starts: bool) -> None:
        """
        Initialize this Game, using p1_starts to find who the first player is.
        If p1_starts is True, it represent player1 is playing.
        """
        side_length = int(input('Please choose side length:(from 1 to 5)'))
        self.current_state = StonehengeState(p1_starts, side_length)

    def get_instructions(self) -> str:
        """
        Return the instructions for this Game.
        """
        return """Stonehenge is played on a hexagonal grid. Boards can have
        various sizes based on their side-length (the number of cells along the
        bottom).Players take turns claiming cells (circles labelled with a
        capital letter). When a player captures at least half of the cells in a
        ley-line (hexagons with a line connecting it to cells), then the player
        captures that ley-line. The first player to capture at least half of
        the ley-lines is the winner.( A ley-line, once claimed, cannot be
        taken by the other player.)
        """

    def is_over(self, state: GameState) -> bool:
        """
        Return whether or not this game is over at state.
        """
        # num is half of the ley-lines.
        # p1,p2 is the sum of marker of each player.
        num = len(state.value[1:])/2
        p1 = p2 = 0
        for item in state.value[1:]:
            if item[0] == '1':
                p1 += 1
            elif item[0] == '2':
                p2 += 1
        return p1 >= num or p2 >= num #or \
               #state.get_possible_moves() == [](don't need to check possi_move)


    def is_winner(self, player: str) -> bool:
        """
        Return whether player has won the game.

        Precondition: player is 'p1' or 'p2'.
        """
        person_win = ''
        #if self.is_over(self.current_state):(client code only check is_winner when game is over)
            # num is half of the ley-lines.
            # p1,p2 is the sum of marker of each player.
            # copy some code from is_over to find who actually wins.
        num = len(self.current_state.value[1:]) / 2
        p1 = p2 = 0
        for item in self.current_state.value[1:]:
            if item[0] == '1':
                p1 += 1
            elif item[0] == '2':
                p2 += 1
        if p1 >= num:
            person_win = 'p1'
        elif p2 >= num:
            person_win = 'p2'

        return person_win == player

    def str_to_move(self, string: str) -> str:
        """
        Return the move that string represents. If string is not a move,
        return some invalid move.
        """
        return str(string)


class StonehengeState(GameState):
    """Create the state of Stonehenge.
    A subclass of class Gamestate."""
    is_p1_turn: bool
    side_length: int
    value: tuple

    def __init__(self, is_p1_turn: bool, side_length: int) -> None:
        """
        Initialize this game state and set the current player based on
        is_p1_turn.

        """
        # side_lenth, is_p1_turn is passed from Game.
        # create self.value for implementing the following methods.
        self.side_length = side_length
        n = self.side_length
        self.is_p1_turn = is_p1_turn
        if n == 1:
            self.value = (""" \
                          @06  @05
                         /   /
                   @01 - A - B
                         \\ / \\
                      @02 - C   @04
                           \\
                            @03""",
                          '@AB', '@C',
                          '@CA', '@B',
                          '@BC', '@A')
        elif n == 2:
            self.value = ("""\
                            @09 @08
                           /   /
                      @01 - A - B   @07
                         / \\ / \\ /
                   @02 - C - D - E
                         \\ / \\ / \\
                      @03 - F - G   @06
                           \\   \\
                            @04   @05""",
                          '@AB', '@CDE', '@FG',
                          '@FC', '@GDA', '@EB',
                          '@EG', '@BDF', '@AC')
        elif n == 3:
            self.value = ("""\
                            @12   @11
                           /   /
                      @01 - A - B   @10
                         / \\ / \\ /
                    @02 - C - D - E   @09
                       / \\ / \\ / \\
                  @03 - F - G - H - I   
                       \\ / \\ / \\ / \\
                     @04 - J - K - L   @08
                           \\   \\   \\
                            @05   @06   @07""",
                          '@AB', '@CDE', '@FGHI', '@JKL',
                          '@JF', '@KGC', '@LHDA', '@IEB',
                          '@IL', '@EHK', '@BDGJ', '@ACF')
        elif n == 4:
            self.value = ("""\
                            @15   @14
                           /   /
                     @01 - A - B   @13
                         / \\ / \\ /
                    @02 - C - D - E   @12
                       / \\ / \\ / \\
                  @03 - F - G - H - I   @11   
                     / \\ / \\ / \\ / \\
              @04 - J - K - L - M - N
                     \\ / \\ / \\ / \\
                @05 - O - P - Q - R   @10
                       \\ / \\ / \\
                        @06   @07   @08    @09""",
                          '@AB', '@CDE', '@FGHI', '@JKLMN', '@OPQR',
                          '@OJ', '@PKF', '@QLGC', '@RMHDA', '@NIEB',
                          '@NR', '@IMQ', '@EHLP', '@BDGKO', '@ACFJ')
        elif n == 5:
            self.value = ("""\
                            @18   @17
                           /   /
                     @01 - A - B   @16
                         / \\ / \\ /
                    @02 - C - D - E   @15
                       / \\ / \\ / \\
                  @03 - F - G - H - I   @14   
                     / \\ / \\ / \\ / \\
              @04 - J - K - L - M - N     @13
                   / \\ / \\ / \\ / \\
            @05 - O -  P -  Q - R  - S - T   
                   \\ / \\ / \\ / \\ / \\
              @06 - U -  V  -  W -  X -  Y   @12
                     \\   \\   \\   \\   \\  
                      @07  @08  @09   @10  @11 """,
                          '@AB', '@CDE', '@FGHI', '@JKLMN', '@OPQRST', '@UVWXY',
                          '@UO', '@VPJ', '@WQKF', '@XRLGC', '@YSMHDA', '@TNIEB',
                          '@TY', '@NSX', '@IMRW', '@EHLQV', '@BDGKPU', '@ACFJO')

    def __str__(self) -> str:
        """
        Return a string representation of the current state of the game.
        """
        # transform '@09',etc to '@' to as to let TA extract self.value.
        n = self.side_length
        trans = [transform(i) for i in range(1, 3*(n+1)+1)]
        # Be careful! self.value is a tuple! Immutable!
        value = self.value[0] # value is the board!
        for j in range(len(trans)):
            if trans[j] in value:
                value = value.replace(trans[j], '@')
        return value

    def get_possible_moves(self) -> List[str]:
        """
        Return all possible moves that can be applied to this state.
        """
        # under the current state, return list unclaimed cells that next player
        # can take.
        result = []
        claim1 = claim2 = 0
        for item in self.value[1:]:
            for char in item:
                if char.isalpha():
                    result.append(char)
            if item[0] == '1':
                claim1 += 1
            elif item[0] == '2':
                claim2 += 1
        # when the game is over, get possible_moves returns empty list.
        num = len(self.value[1:]) / 2
        if claim1 < num and claim2 < num:
            result = remove_dup(result)
            return result
        # if game is over, return []
        return []

    def get_current_player_name(self) -> str:
        """
        Return 'p1' if the current player is Player 1, and 'p2' if the current
        player is Player 2.
        """
        if self.is_p1_turn:
            return 'p1'
        return 'p2'

    def make_move(self, move: str) -> 'StonehengeState':
        """
        Return the GameState that results from applying move to this GameState.
        """
        # move is something like 'A', "B','C'
        # func inside a class is called method!
        # convert self.value to a list
        value = list(self.value)
        claim = '1'
        if not self.is_p1_turn:
            claim = '2'
        # change the value of rows,diagonals (captial letter)in value
        for i in range(len(value)):
            if move in value[i]:
                value[i] = value[i].replace(move, claim)
        #  change corresponding '@' in the whole list
        for i in range(1, len(value)):
            num = (len(value[i])-1)/2
            if value[i].count(claim) >= num:
                value[i] = value[i].replace('@', claim)
                marker = transform(i)
                value[0] = value[0].replace(marker, claim)
        re_value = tuple(value)
        # return a new state
        result = StonehengeState(not self.is_p1_turn, self.side_length)
        result.value = re_value
        return result

    def is_valid_move(self, move: Any) -> bool:
        """
        Return whether move is a valid move for this GameState.
        """
        return move in self.get_possible_moves()

    def __repr__(self) -> Any:
        """
        Return a representation of this state (which can be used for
        equality testing).
        """
        return 'StonghengeState:{}, current_player:{}'.\
            format(str(self.value[0]), self.get_current_player_name())

    def rough_outcome(self) -> float:
        """
        Return an estimate in interval [LOSE, WIN] of best outcome the current
        player can guarantee from state self.
        """
        # If there is even one move that enable the current player to win at
        # once,  return 1.
        # If the other player is able to win immediately no matter what move we
        # make, return -1.
        moves = self.get_possible_moves()
        person_win = []
        for move in moves:
            new_state = self.make_move(move)
            # copy some code (is_over) to find who actually wins in new state.
            num = len(new_state.value[1:]) / 2
            p1 = p2 = 0
            for item in new_state.value[1:]:
                if item[0] == '1':
                    p1 += 1
                elif item[0] == '2':
                    p2 += 1
            if p1 >= num:
                person_win.append('p1')
            elif p2 >= num:
                person_win.append('p2')
        # returns -1 for a state that's over and where the current player is
        # the loser
        winner = ''
        if moves == []:
            num_ = len(self.value[1:]) / 2
            p1_ = p2_ = 0
            for item in self.value[1:]:
                if item[0] == '1':
                    p1_ += 1
                elif item[0] == '2':
                    p2_ += 1
            if p1_ >= num_:
                winner = 'p1'
            elif p2_ >= num_:
                winner = 'p2'
        if moves != [] and ((self.is_p1_turn and 'p1' not in person_win) or
                            (not self.is_p1_turn and 'p2' not in person_win)):
            return -1
        elif moves == [] and ((self.is_p1_turn and winner == 'p2') or
                              (not self.is_p1_turn and winner == 'p1')):
            return -1
        elif moves != [] and ((self.is_p1_turn and 'p1' in person_win) or
                              (not self.is_p1_turn and 'p2' in person_win)):
            return 1
        return 0


# helper func : remove duplicate of a list.
def remove_dup(list1: list)->list:
    """Return a list after removing all the duplicates of a list.
    >>> lst = remove_dup(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'F', 'C', 'G', 'D',
     'A', 'E', 'B', 'E', 'G', 'B', 'D', 'F', 'A', 'C'])
    >>> lst.sort()
    >>> lst
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']"""
    tem = set(list1)
    return list(tem)


# helper func: transform index to corresponding markers.
def transform(i: int)->str:
    """Return corresponding markers according to index.
    >>> transform(9)
    '@09'
    >>> transform(25)
    '@25'
    """
    if i <= 9:
        return '@0' + str(i)
    return '@' + str(i)


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
