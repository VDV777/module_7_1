# Задача "Учёт товаров":
# Необходимо реализовать 2 класса Product и Shop, с помощью которых будет производиться запись в файл с продуктами.
# Объекты класса Product будут создаваться следующим образом - Product('Potato', 50.0, 'Vagetables') и обладать следующими свойствами:
# Атрибут name - название продукта (строка).
# Атрибут weight - общий вес товара (дробное число) (5.4, 52.8 и т.п.).
# Атрибут category - категория товара (строка).
# Метод __str__, который возвращает строку в формате '<название>, <вес>, <категория>'. Все данные в строке разделены запятой с пробелами.
#
# Объекты класса Shop будут создаваться следующим образом - Shop() и обладать следующими свойствами:
# Инкапсулированный атрибут __file_name = 'products.txt'.
# Метод get_products(self), который считывает всю информацию из файла __file_name, закрывает его и возвращает единую строку со всеми товарами из файла __file_name.
# Метод add(self, *products), который принимает неограниченное количество объектов класса Product. Добавляет в файл __file_name каждый продукт из products, если его ещё нет в файле (по названию). Если такой продукт уже есть, то не добавляет и выводит строку 'Продукт <название> уже есть в магазине' .
import os.path


class Product:

    def __init__(self, name: str, weight: float, category: str):

        self.name: str = name
        self.weight: float = weight
        self.category: str = category

    def __str__(self):

        return f'{self.name} {self.weight} {self.category}'


class Shop:

    def __init__(self):

        self.__file_name: str = 'products.txt'
        self.__productList: list[Product] = []

        self.get_products()

    def get_products(self) -> None:

        try:
            if os.path.exists(self.__file_name):
                with open(file=self.__file_name, mode='r', encoding='UTF-8') as file:

                    for line in file.readlines():
                        self.__productList += [line.strip('\n')]

        except Exception as e:
            print(e)

    def add(self, productList: list[Product]):

        for product in productList:

            if product.__str__() not in self.__productList:

                try:
                    with open(file=self.__file_name, mode='a', encoding='UTF-8') as file:
                        file.write(product.__str__() + '\n')

                except Exception as e:
                    print(e)

                self.__productList += [product.__str__()]
            else:
                print(f'Продукт <{product.name}> уже есть в магазине')


Shop().add([Product('apple', 30.0, 'fruit'), Product('tomato', 10.0, 'vegetable')])


