from src.item import Item

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv('отсутствующий_файл.csv')
    # FileNotFoundError: Отсутствует файл отсутствующий_файл.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv('items_broken.csv')
    # InstantiateCSVError: Файл items_broken.csv поврежден
