from rational import Rational
from rational_list import RationalList
from rational_list_iterator import RationalListIterator

class RationalListExtended(RationalList):
    def __iter__(self):
        return RationalListIterator(self.numbers) 