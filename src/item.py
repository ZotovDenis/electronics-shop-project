from csv import DictReader
import os


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
            print("Длина наименования товара превышает 10 символов.")

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса Item из файла csv.
        """
        cls.all.clear()
        file = os.path.join('..', 'src', 'items.csv')
        with open(file, 'r') as csv_file:
            csv_reader = DictReader(csv_file)
            for row in csv_reader:
                name, price, quantity = row['name'], float(row['price']), int(row['quantity'])
                cls(name, price, quantity)

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
