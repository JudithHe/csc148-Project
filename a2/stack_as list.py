""" implement stack ADT
"""
# from container import Container, EmptyContainerException
# from typing import Any

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
            raise EmptyContainerException
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
