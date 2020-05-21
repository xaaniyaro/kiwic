from ShifterFactory import Creator, CircularShifterCreator
from Input import Input

def client_code(creator: Creator, entrada) -> None:
    print("Client: I'm not aware of the creator's class, but it still works.")
    print(creator.some_operation(entrada))

if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    inp = Input().txtFile('ex1.txt')
    client_code(CircularShifterCreator(), inp)
    print("\n")