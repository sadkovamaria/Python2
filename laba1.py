import doctest
from abc import ABC, abstractmethod


# TODO Написать 3 класса с документацией и аннотацией типов


class Vehicle(ABC):
    def __init__(self, max_speed: float, fuel: float):
        """
        Абстрактный класс "Транспорт"

        :param max_speed: Максимальная скорость
        :param fuel: Количество топлива

        Примеры:
        >>> class Car(Vehicle):
        ...     def start_engine(self): ...
        ...     def drive(self, distance: float): ...
        ...     def refuel(self, amount: float): ...
        >>> car = Car(120, 10)
        """
        if not isinstance(max_speed, (int, float)):
            raise TypeError("Скорость должна быть числом")
        if max_speed <= 0:
            raise ValueError("Скорость должна быть положительной")
        self.max_speed = max_speed

        if not isinstance(fuel, (int, float)):
            raise TypeError("Топливо должно быть числом")
        if fuel < 0:
            raise ValueError("Топливо не может быть отрицательным")
        self.fuel = fuel

    @abstractmethod
    def start_engine(self) -> None:
        """
        Запуск двигателя

        :return: None

        Примеры:
        >>> class Car(Vehicle):
        ...     def start_engine(self): ...
        ...     def drive(self, distance: float): ...
        ...     def refuel(self, amount: float): ...
        >>> car = Car(120, 10)
        >>> car.start_engine()
        """
        ...

    @abstractmethod
    def drive(self, distance: float) -> None:
        """
        Поездка на расстояние

        :param distance: расстояние поездки
        :return: None

        Примеры:
        >>> class Car(Vehicle):
        ...     def start_engine(self): ...
        ...     def drive(self, distance: float): ...
        ...     def refuel(self, amount: float): ...
        >>> car = Car(120, 10)
        >>> car.drive(50)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError("Расстояние должно быть числом")
        if distance < 0:
            raise ValueError("Расстояние не может быть отрицательным")
        ...

    @abstractmethod
    def refuel(self, amount: float) -> None:
        """
        Заправка топливом

        :param amount: количество топлива
        :return: None

        Примеры:
        >>> class Car(Vehicle):
        ...     def start_engine(self): ...
        ...     def drive(self, distance: float): ...
        ...     def refuel(self, amount: float): ...
        >>> car = Car(120, 10)
        >>> car.refuel(20)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Количество топлива должно быть числом")
        if amount <= 0:
            raise ValueError("Количество топлива должно быть положительным")
        ...


class BankAccount(ABC):
    def __init__(self, balance: float, account_number: str):
        """
        Абстрактный класс "Банковский счет"

        :param balance: Баланс счета
        :param account_number: Номер счета

        Примеры:
        >>> class MyAccount(BankAccount):
        ...     def deposit(self, amount: float): ...
        ...     def withdraw(self, amount: float): ...
        ...     def check_balance(self) -> float: return 0
        >>> acc = MyAccount(100, "123")
        """
        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть числом")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.balance = balance

        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть строкой")
        if not account_number:
            raise ValueError("Номер счета не может быть пустым")
        self.account_number = account_number

    @abstractmethod
    def deposit(self, amount: float) -> None:
        """
        Пополнение счета

        :param amount: сумма пополнения
        :return: None

        Примеры:
        >>> class MyAccount(BankAccount):
        ...     def deposit(self, amount: float): ...
        ...     def withdraw(self, amount: float): ...
        ...     def check_balance(self) -> float: return 0
        >>> acc = MyAccount(100, "123")
        >>> acc.deposit(50)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        ...

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        """
        Снятие денег

        :param amount: сумма снятия
        :return: None

        Примеры:
        >>> class MyAccount(BankAccount):
        ...     def deposit(self, amount: float): ...
        ...     def withdraw(self, amount: float): ...
        ...     def check_balance(self) -> float: return 0
        >>> acc = MyAccount(100, "123")
        >>> acc.withdraw(30)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        ...

    @abstractmethod
    def check_balance(self) -> float:
        """
        Проверка баланса

        :return: текущий баланс

        Примеры:
        >>> class MyAccount(BankAccount):
        ...     def deposit(self, amount: float): ...
        ...     def withdraw(self, amount: float): ...
        ...     def check_balance(self) -> float: return 100
        >>> acc = MyAccount(100, "123")
        >>> acc.check_balance()
        100
        """
        ...


class Stack(ABC):
    def __init__(self, capacity: int):
        """
        Абстрактный класс "Стек"

        :param capacity: Максимальный размер

        Примеры:
        >>> class MyStack(Stack):
        ...     def push(self, item): ...
        ...     def pop(self): ...
        ...     def peek(self): ...
        >>> s = MyStack(10)
        """
        if not isinstance(capacity, int):
            raise TypeError("Размер должен быть int")
        if capacity <= 0:
            raise ValueError("Размер должен быть положительным")
        self.capacity = capacity

    @abstractmethod
    def push(self, item: object) -> None:
        """
        Добавление элемента

        :param item: элемент
        :return: None

        Примеры:
        >>> class MyStack(Stack):
        ...     def push(self, item): ...
        ...     def pop(self): ...
        ...     def peek(self): ...
        >>> s = MyStack(10)
        >>> s.push(1)
        """
        ...

    @abstractmethod
    def pop(self) -> object:
        """
        Удаление элемента

        :return: удаленный элемент

        Примеры:
        >>> class MyStack(Stack):
        ...     def push(self, item): ...
        ...     def pop(self): return None
        ...     def peek(self): ...
        >>> s = MyStack(10)
        >>> s.pop()
        """
        ...

    @abstractmethod
    def peek(self) -> object:
        """
        Просмотр верхнего элемента

        :return: верхний элемент

        Примеры:
        >>> class MyStack(Stack):
        ...     def push(self, item): ...
        ...     def pop(self): ...
        ...     def peek(self): return None
        >>> s = MyStack(10)
        >>> s.peek()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass