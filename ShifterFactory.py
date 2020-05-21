from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory method.
        """
        pass

    def some_operation(self, sentences) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory method.
        Subclasses can indirectly change that business logic by overriding the
        factory method and returning a different type of product from it.
        """

        # Call the factory method to create a Product object.
        product = self.factory_method()

        # Now, use the product.
        result = product.shift(sentences)

        return result


class CircularShifterCreator(Creator):
    def factory_method(self) -> CircularShifter:
        return CircularShifter()


class Shifter(ABC):
    @abstractmethod
    def shift(self) -> str:
        pass

"""ConcreteShifter"""
class CircularShifter(Shifter):
    def generateString(self, words):
        sentence = words[0]
        for i in range(len(words)-1):
            sentence = sentence + " " + words[i+1]
        return sentence
    
    def shift(self, sentencesList) -> str:
        shifts = []
        for sentence in sentencesList:
            for i in range(len(sentence)):
                shifts.append(self.generateString(sentence))
                firstElement = sentence.pop(0)
                sentence.append(firstElement)
        return shifts
    