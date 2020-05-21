from ShifterFactory import Creator, CircularShifterCreator
from Input import Input

def client_code(creator: Creator, entrada) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print("Client: I'm not aware of the creator's class, but it still works.")
    print(creator.some_operation(entrada))

if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    inp = Input().txtFile('ex1.txt')
    client_code(CircularShifterCreator(), inp)
    print("\n")