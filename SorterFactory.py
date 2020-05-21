from __future__ import annotations
from abc import ABC, abstractmethod

class SorterCreator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self, sentences) -> str:
        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = product.sort(sentences)

        return result

class AscendingSortCreator(SorterCreator):
    def factory_method(self) -> AscendingSorter:
        return AscendingSorter()

class DescendingSortCreator(SorterCreator):
    def factory_method(self) -> DescendingSorter:
        return DescendingSorter()

class Sorter(ABC):
    @abstractmethod
    def sort(self) -> str:
        pass

class AscendingSorter(Sorter):
    def sort(self, shifts) -> str:
        sortList = sorted(shifts)
        return sortList

class DescendingSorter(Sorter):
    def sort(self, shifts) -> str:
        sortList = sorted(shifts, reverse = True)
        return sortList
