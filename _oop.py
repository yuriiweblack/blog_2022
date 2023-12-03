
#!/usr/bin/python3
from abc import ABC, abstractmethod

class Shop(ABC):
    """
        Product shop
    """

    __info_shop = "Product shop"

    open_shop_time = 8
    closed_shop_time = 22

    @abstractmethod
    def director(self):
        return "OWN Director"

    @classmethod
    def cheeck_time(cls, time):
        return cls.open_shop_time < time and time < cls.closed_shop_time

    def __init__(self, name, location):
        self.name = name
        self.location = location

    # def __str__(self):
    #     return f'Shop {self.name.title()}, Location: {self.location}!!!'

    def __repr__(self):
        return f'Shop {self.name.title()}, Location: {self.location}!!!'

    def open_shop(self, time):
        if self.cheeck_time(time):
            return "Shop is open!"
        else:
            return "Shop closed!"
        # return True if self.cheeck_time(time) else False

    @staticmethod
    def culc(num_1, num_2):
        return num_1 + num_2

    @property
    def show_atrr(self):
        return self.__info_shop



class ShopBuild(Shop):

    def __init__(self, name, location, type):
        super().__init__(name, location)
        self.type = type

    def info(self):
        return f"ShopBuild: {self.type}"

    def director(self, name):
        return f"{name} - Director!!!"



if __name__ == '__main__':
    shop_build = ShopBuild("Epik", "Kiev", "Building construction")
    print(shop_build.director("Max"))

    # name = input("Enter name shop: ")
    # location = input("Enter name location: ")
    # shop_1 = Shop(name, location)
    # print(shop_1)
    # print(shop_1.open_shop(7))
    print(Shop.culc(10,30))
