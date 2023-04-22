from __future__ import annotations

from abc import ABC, abstractmethod


class Order:
    """ Context """

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        print('Tentando executar pending...')
        self.state.pending()
        print('Estado atual: ', self.state)
        print()

    def approve(self):
        print('Tentando executar pending...')
        self.state.approve()
        print('Estado atual: ', self.state)
        print()

    def reject(self):
        print('Tentando executar pending...')
        self.state.reject()
        print('Estado atual: ', self.state)
        print()


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass

    def __str__(self):
        return self.__class__.__name__


class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento está pendente')

    def approve(self) -> None:
        self.order.state = PaymentApprove(self.order)
        print('Pagamento aprovado')

    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print('Pagamento recusado')


class PaymentApprove(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento pendente')

    def approve(self) -> None:
        print('Pagamento já foi aprovado')

    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print('Pagamento recusado')


class PaymentReject(OrderState):
    def pending(self) -> None:
        print('Pagamento recusado. Não é possivel realizar a ação.')

    def approve(self) -> None:
        print('Pagamento recusado. Não é possivel realizar a ação.')

    def reject(self) -> None:
        print('Pagamento recusado. Não é possivel realizar a ação.')


if __name__ == "__main__":
    order = Order()
    order.pending()
    order.approve()
    order.pending()
    order.reject()
    order.pending()
    order.approve()
