from wine import Wine
from beer import Beer
from market import Market

"""

TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""
wines = [
    Wine("Piemonte", "1981-12-01"),
    Wine("Sassicaia", "2020-04-12"),
    Wine("Pasqua Montepulciano Abruzzo", "2022-07-16"),
    Wine("Noble Vigne Grenache", "2023-09-12"),
    Wine("Pavillon Rouge du Chateau Margaux", "1996-11-01"),
    Wine("Marchesini Asti", "2022-11-04"),
    Wine("Pasqua Pinot Grigio", "2012-04-23"),
    Wine("Pasqua Bardolino", "2018-03-29"),
    Wine("Mayoral Monastrell", "2019-05-11")
]

beers = [
    Beer("Bud", "2023-04-22"),
    Beer("Hollandia", "2023-06-02"),
    Beer("Cernovar", "2023-02-02"),
    Beer("Faxe Premium", "2023-03-08"),
    Beer("El Capulco", "2023-10-21"),
    Beer("Corona extra", "2023-01-14"),
    Beer("Claro", "2023-04-18"),
    Beer("Zatecky Gus", "2023-09-08"),
]

market = Market(wines, beers)

# * получить список всех напитков (вина и пива) отсортированный по наименованию
print(market.get_drinks_sorted_by_title())

# * проверить наличие напитка в магазине (за время О(1))
print(market.has_drink_with_title("Corona extra"))
print(market.has_drink_with_title("bjhbj"))

# * получить список напитков (вина и пива) в указанном диапазоне даты производства
print(market.get_drinks_by_production_date("2023-09-08", "2023-09-12"))
print(market.get_drinks_by_production_date("2023-09-08"))

