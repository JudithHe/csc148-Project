"""
A module for strategies.

NOTE: Make sure this file adheres to python-ta.
Adjust the type annotations as needed, and implement both a recursive
and an iterative version of minimax.
"""
# Cite: The class Stack at the bottom is taken from classes.
from typing import Any



# TODO: Adjust the type annotation as needed.
def interactive_strategy(game: Any) -> str:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)

def rough_outcome_strategy(game: Any) -> Any:
    """
    Return a move for game by picking a move which results in a state with
    the lowest rough_outcome() for the opponent.

    NOTE: game.rough_outcome() should do the following:
        - For a state that's over, it returns the score for the current
          player of that state.
        - For a state that's not over:
            - If there is a move that results in the current player winning,
              return 1.
            - If all moves result in states where the other player can
              immediately win, return -1.
            - Otherwise; return a number between -1 and 1 corresponding to how
              'likely' the current player will win from the current state.

        In essence: rough_outcome() will only look 1 or 2 states ahead to
        'guess' the outcome of the game, but no further. It's better than
        random, but worse than minimax.
    """
    current_state = game.current_state
    best_move = None
    best_outcome = -2  # Temporarily -- just so we can replace this easily later

    # Get the move that results in the lowest rough_outcome for the opponent
    for move in current_state.get_possible_moves():
        new_state = current_state.make_move(move)

        # We multiply the below by -1 since a state that's bad for the opponent
        # is good for us.
        guessed_score = new_state.rough_outcome() * -1
        if guessed_score > best_outcome:
            best_outcome = guessed_score
            best_move = move

    # Return the move that resulted in the best rough_outcome
    return best_move

def minimax_recursive_strategy(game: Any) -> str:
    """Return a move that produces a "highest guaranteed score" at each step
    for the current player."""
    current_state = game.current_state
    possible_moves = current_state.get_possible_moves()
    dict_to_compare = {}
    move = ''  # set move to an initial value temporarily.
    for move in possible_moves:
        next_state = current_state.make_move(move)
        state_score = highest_score(next_state, game)
        #move_score for each next_state = -1 * state_score
        move_score = -1 * state_score
        dict_to_compare[move] = move_score
    for move in dict_to_compare:
        if dict_to_compare[move] == highest_score(current_state, game):
            return move
    # python is silly so I return an '' although it will have get to
    # this point by logic!
    return ''


# recursive helper func
def highest_score(current_state: 'GameState', game: Any)->int:
    """Return a highest-guaranteed-score(state_score) for the current_state.
    """
    possible_moves = current_state.get_possible_moves()
    tem = []  # a temporary list for data
    if possible_moves == []:  # the game is over
        if game.is_winner(current_state.get_current_player_name()):
            return 1
        elif not game.is_winner(current_state.get_current_player_name()):
            return -1
        return 0

    # else part: find the state_score of supertree node,current_state.
    for move in possible_moves:
        next_state = current_state.make_move(move)
        move_score = (-1) * highest_score(next_state, game)
        tem.append(move_score)
    return max(tem)


# TODO: Implement an iterative version of the minimax strategy.
def minimax_iterative_strategy(game: Any) -> str:
    """Return the best move for the current state and the current player."""
    # add data to stack.
    current_state = game.current_state
    # Use stack to keep track of state of different levels.
    stack = Stack()
    # Use dictionary to keeptrack of state_score.
    dict1 = {}
    stack.add(current_state)
    while not stack.is_empty():
        check_state = stack.remove()
        # state_score must be obtained by checking whether the over-state's
        # player is the winner of game.
        if check_state.get_possible_moves() == []:
            if game.is_winner(check_state.get_current_player_name()):
                state_score = 1
            elif not game.is_winner(check_state.get_current_player_name()):
                state_score = -1
            else:
                state_score = 0
            dict1[str(check_state)] = state_score
        else:

            stack.add(check_state)
            # child_states have been checked, remove it, add to dict
            check = all([str(check_state.make_move(move)) in dict1.keys()
                         for move in check_state.get_possible_moves()])
            if check:
                stack.remove()
                children = [str(check_state.make_move(move))
                            for move in check_state.get_possible_moves()]
                # get the state_score of check_state
                state_score = max([-1 * dict1[key] for key in children])
                dict1[str(check_state)] = state_score
            else:
                for move in check_state.get_possible_moves():
                    stack.add(check_state.make_move(move))
        # print(len(stack))
        # print(dict1.items())
    # find the best move for current state. best_move store move_store for each
    # move.
    best_move = {}
    for move in current_state.get_possible_moves():
        child_state_score = dict1[str(current_state.make_move(move))]
        move_score = -1 * child_state_score
        best_move[move] = move_score
    max_num = max(list(best_move.values()))
    for key in best_move:
        if best_move[key] == max_num:
            return key
    # python is silly so I return an '' though by logic it will have get to
    # this point!
    return ''


# helper data structure Stack() cited from class
class Stack():
    """ Last-in, first-out (LIFO) stack.
    """

    def __init__(self) -> None:
        """ Create a new, empty Stack self.
        """
        self._storage = []

    def add(self, obj: object)-> None:
        """ Add object obj to top of Stack self.
        """
        self._storage.append(obj)

    def remove(self) -> object:
        """
        Remove and return top element of Stack self.

        Assume Stack self is not empty, otherwise
        raises EmptyStackException
        >>> s = Stack()
        >>> s.add(5)
        >>> s.add(7)
        >>> s.remove()
        7
        """
        if self.is_empty():
            raise Exception
        else:
            return self._storage.pop()

    def is_empty(self) -> bool:
        """
        Return whether Stack self is empty.
        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.add(s)
        >>> s.is_empty()
        False
        """
        return len(self._storage) == 0

    # def __len__(self)->int:
    #     """Return the number of elements in stack.
    #     >>> s = Stack()
    #     >>> s.add(5)
    #     >>> s.add(7)
    #     >>> s.remove()
    #     7
    #     >>> len(s)
    #     1"""
    #     return len(self._storage)


if __name__ == "__main__":
    from python_ta import check_all
    check_all(config="a2_pyta.txt")
