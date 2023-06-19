from src.item import Item, InstantiateCSVError

if __name__ == '__main__':
    try:
        Item.instantiate_from_csv()
    except FileNotFoundError as e:
        print(e)
    except InstantiateCSVError as ex:
        print(ex.message)
