from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self) -> None:
        self.hook()
        self.operation_1()
        self.base_class_method()
        self.operation_2()

    def hook(self): pass

    def base_class_method(self):
        print('Class Abstract')

    @abstractmethod
    def operation_1(self): pass

    @abstractmethod
    def operation_2(self): pass


class ConcreteClass_1(Abstract):
    def hook(self):
        print('hook')

    def operation_1(self):
        print('Op 1 concluido')

    def operation_2(self):
        print('Op 2 concluido')


class ConcreteClass_2(Abstract):
    def operation_1(self):
        print('Op 1 concluido (de maneira diferente)')

    def operation_2(self):
        print('Op 2 concluido (de maneira diferente)')


if __name__ == "__main__":
    c1 = ConcreteClass_1()
    c1.template_method()

    print()

    c2 = ConcreteClass_2()
    c2.template_method()
