from decorator import time_decorator
class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = wines
        self.beers = beers
        self.drinks = self.get_dict_drinks(wines + beers)
        pass

    @time_decorator
    def get_dict_drinks(self, drinks: list) -> dict:
        """
        Метод получения словаря напитков
        :param drinks:
        :return: dict
        """
        dict = {}
        for drink in drinks:
            dict[drink.title] = drink.production_date
        return dict
    
    @time_decorator
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.drinks

    @time_decorator
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        all_drinks = list(self.drinks.keys())
        return sorted(all_drinks)

    @time_decorator
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        all_drinks = list(self.drinks.items())
        filtered_drinks = []
        for drink in all_drinks:
            if from_date and drink[1] < from_date:
                continue
            if to_date and to_date < drink[1]:
                continue
            filtered_drinks.append(drink)    
        return filtered_drinks
