Stonehenge is played on a hexagonal grid. Boards can have
        various sizes based on their side-length (the number of cells along the
        bottom).Players take turns claiming cells (circles labelled with a
        capital letter). When a player captures at least half of the cells in a
        ley-line (hexagons with a line connecting it to cells), then the player
        captures that ley-line. The first player to capture at least half of
        the ley-lines is the winner.( A ley-line, once claimed, cannot be
        taken by the other player.)



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
