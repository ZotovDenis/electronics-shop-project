import os
from csv import DictReader


class InstantiateCSVError(Exception):
    """Класс для отработки исключения с поврежденным файлом items.csv"""

    def __init__(self, *args):
        self.message = args[0] if not None else "Файл поврежден"


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        try:
            if len(new_name) <= 10:
                self.__name = new_name
        except ValueError:
            raise ValueError("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls, filename='items.csv'):
        """
        Инициализирует экземпляры класса Item из файла csv.
        """
        cls.all.clear()
        file = os.path.join(os.path.dirname(__file__), filename)
        try:
            with open(file, 'r', encoding='windows-1251') as csv_file:
                csv_reader = DictReader(csv_file)
                for row in csv_reader:
                    try:
                        name, price, quantity = row['name'], float(row['price']), int(row['quantity'])
                        cls(name, price, quantity)
                    except (ValueError, KeyError):
                        raise InstantiateCSVError(f"Файл {filename} поврежден")

        except FileNotFoundError:
            raise FileNotFoundError(f"Отсутствует файл {filename}")

    @staticmethod
    def string_to_number(number):
        """
        Преобразует строку в число.

        :param number: Строка, которую нужно преобразовать в число.
        :return: Число.
        """
        try:
            return int(number)
        except ValueError:
            if number.isalpha() or number == "":
                return False
            else:
                return int(float(number))

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None
