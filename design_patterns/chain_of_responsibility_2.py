from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self) -> None:
        self.sucessor: Handler

    @abstractmethod
    def handle(self, letter: str) -> str: pass


class HandlerABC(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['A', 'B', 'C']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'HandlerABC: conseguiu tratar o valor {letter}'
        return self.sucessor.handle(letter)


class HandlerDEF(Handler):
    def __init__(self, sucessor: Handler) -> None:
        self.letters = ['D', 'E', 'F']
        self.sucessor = sucessor

    def handle(self, letter: str) -> str:
        if letter in self.letters:
            return f'HandlerDEF: conseguiu tratar o valor {letter}'
        return self.sucessor.handle(letter)


class HandlerUnsolved(Handler):
    def handle(self, letter: str) -> str:
        return f'HandlerUnsolved: não conseguiu tratar o valor {letter}'


if __name__ == "__main__":
    hander_unsolved = HandlerUnsolved()
    handler_def = HandlerDEF(hander_unsolved)
    handler_abc = HandlerABC(handler_def)

    print(handler_abc.handle('A'))
    print(handler_abc.handle('B'))
    print(handler_abc.handle('C'))
    print(handler_abc.handle('D'))
    print(handler_abc.handle('E'))
    print(handler_abc.handle('F'))
    print(handler_abc.handle('G'))
    print(handler_abc.handle('H'))
    print(handler_abc.handle('I'))

    print()
    print(handler_def.handle('A'))
    print(handler_def.handle('B'))
    print(handler_def.handle('C'))
    print(handler_def.handle('D'))
    print(handler_def.handle('E'))
    print(handler_def.handle('F'))
    print(handler_def.handle('G'))
    print(handler_def.handle('H'))
    print(handler_def.handle('I'))

    print()
    print(hander_unsolved.handle('A'))
    print(hander_unsolved.handle('B'))
    print(hander_unsolved.handle('C'))
    print(hander_unsolved.handle('D'))
    print(hander_unsolved.handle('E'))
    print(hander_unsolved.handle('F'))
    print(hander_unsolved.handle('G'))
    print(hander_unsolved.handle('H'))
    print(hander_unsolved.handle('I'))
