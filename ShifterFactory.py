from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self, sentences) -> str:
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
    