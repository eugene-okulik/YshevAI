"""Задание
Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
Создать экземпляры (объекты) цветов разных видов. Собрать букет (букет - еще один класс) с определением его стоимости.
В букете цветы пусть хранятся в списке. Это будет список объектов.
Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)
(это тоже методы)
Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).
"""


import abc
import random


class Flowers(abc.ABC):
    """Родительский класс"""
    def __init__(self, length, life_time, color, cost):
        self.length = length
        self.color = color
        self.life_time = life_time
        self.cost = cost if cost else self.get_flower_cost()
        self.name = ""

    def _get_flower_len_rng(self, min_len, mid_len):
        """Возвращает группу по длине"""
        if self.length <= min_len:
            return "short"
        elif min_len < self.length <= mid_len:
            return "middle"
        else:
            return "long"

    def _get_length_coef(self):
        """В зависимости от длины стебля возвращаетс срок жизни для цветов"""
        match self.get_flower_rng():
            case "short":
                return 0
            case "middle":
                return 0.1
            case "long":
                return 0.2

    def _get_flower_cost(self, short, middle, long):
        """В зависимости от длины стебля возвращается цена цветка,
        Имеется в виду, что разные сорты имеют разную длину стебля"""
        match self.get_flower_rng():
            case "short":
                return short
            case "middle":
                return middle
            case "long":
                return long

    @abc.abstractmethod
    def get_flower_cost(self):
        pass

    @abc.abstractmethod
    def get_flower_rng(self):
        pass

    @abc.abstractmethod
    def get_life_time(self):
        """Остаточный срок жизни с учетом длины стебля"""
        return self.life_time - self.life_time * self._get_length_coef()

    def __repr__(self):
        return (f"{self.name} < Длина стебля: {self.length} см., До увядания: {self.life_time} д., Цвет: {self.color}, "
                f"Стоимость: {self.cost} руб. >")


class Tulip(Flowers):
    def __init__(self, length, life_time, color, cost=0):
        super().__init__(length, life_time, color, cost)
        self.name = 'Тюльпан'
        self.length = length
        self.life_time = 10 - life_time if life_time <= 10 else 0

    def get_flower_rng(self):
        return Flowers._get_flower_len_rng(self, 15, 30)

    def get_life_time(self):
        return Flowers.get_life_time(self)

    def get_flower_cost(self):
        return Flowers._get_flower_cost(self, 150, 220, 300)


class Peony(Flowers):
    def __init__(self, length, life_time, color, cost=0):
        super().__init__(length, life_time, color, cost)
        self.name = 'Пион'
        self.length = length
        self.life_time = 7 - life_time if life_time <= 7 else 0

    def get_flower_rng(self):
        return Flowers._get_flower_len_rng(self, 70, 100)

    def get_life_time(self):
        return Flowers.get_life_time(self)

    def get_flower_cost(self):
        return Flowers._get_flower_cost(self, 150, 300, 500)


class Rose(Flowers):
    def __init__(self, length, life_time, color, cost=0):
        super().__init__(length, life_time, color, cost)
        self.name = 'Роза'
        self.length = length
        self.life_time = 15 - life_time if life_time <= 15 else 0

    def get_flower_rng(self):
        return Flowers._get_flower_len_rng(self, 40, 70)

    def get_life_time(self):
        return Flowers.get_life_time(self)

    def get_flower_cost(self):
        return Flowers._get_flower_cost(self, 220, 450, 600)


class Chrysanthemums(Flowers):
    def __init__(self, length, life_time, color, cost=0):
        super().__init__(length, life_time, color, cost)
        self.name = 'Хризантема'
        self.length = length
        self.life_time = 15 - life_time if life_time <= 15 else 0

    def get_flower_rng(self):
        return Flowers._get_flower_len_rng(self, 40, 80)

    def get_life_time(self):
        return Flowers.get_life_time(self)

    def get_flower_cost(self):
        return Flowers._get_flower_cost(self, 150, 250, 500)


class Gerbera(Flowers):
    def __init__(self, length, life_time, color, cost=0):
        super().__init__(length, life_time, color, cost)
        self.name = 'Гербера'
        self.length = length
        self.life_time = 15 - life_time if life_time <= 15 else 0

    def get_flower_rng(self):
        return Flowers._get_flower_len_rng(self, 20, 40)

    def get_life_time(self):
        return Flowers.get_life_time(self)

    def get_flower_cost(self):
        return Flowers._get_flower_cost(self, 220, 280, 350)


def get_flowers_for_bouquet(count: int) -> list:
    colors = ["белый", "синий", "розовый", "красный", "оранжевый", "желтый", "фиолетовый", "бордовый"]
    flowers_list = []

    for _ in range(count):
        flowers_obj = [Tulip(length=random.randint(8, 60), life_time=random.randint(0, 10),
                             color=random.choice(colors)),
                       Peony(length=random.randint(50, 120), life_time=random.randint(0, 7),
                             color=random.choice(colors)),
                       Rose(length=random.randint(30, 100), life_time=random.randint(0, 15),
                            color=random.choice(colors)),
                       Chrysanthemums(length=random.randint(30, 100), life_time=random.randint(0, 15),
                                      color=random.choice(colors)),
                       Gerbera(length=random.randint(15, 60), life_time=random.randint(0, 15),
                               color=random.choice(colors))]

        flowers_list.append(random.choice(flowers_obj))
    return flowers_list


class Bouquet:
    """Букет"""

    def __init__(self, flowers: list):
        self.flowers = flowers
        self.flowers_life_time = [flower.life_time for flower in self.flowers]
        self.flowers_cost = [flower.cost for flower in self.flowers]
        self._by_life_time = ""
        self._by_color = ""
        self._by_length = ""
        self._by_cost = ""
        self._by_name = ""

    @property
    def bouquet_life_time(self):
        return f'Средняя продолжительность жизни букета: {round(sum(self.flowers_life_time) / len(self.flowers))} д.'

    @property
    def sort_by_life_time(self):
        return sorted(self.flowers, key=lambda f: f.life_time)

    @property
    def sort_by_color(self):
        return sorted(self.flowers, key=lambda f: f.color)

    @property
    def sort_by_length(self):
        return sorted(self.flowers, key=lambda f: f.length)

    @property
    def sort_by_cost(self):
        return sorted(self.flowers, key=lambda f: f.cost)

    @property
    def sort_by_name(self):
        return sorted(self.flowers, key=lambda f: f.name)

    @property
    def cost(self):
        return f'Стоимость: {sum(self.flowers_cost)} руб.'

    @property
    def get_by_life_time(self):
        return self._by_life_time

    @get_by_life_time.setter
    def get_by_life_time(self, value):
        self._by_life_time = [i for i in self.flowers if i.life_time == value]

    @property
    def get_by_color(self):
        return self._by_color

    @get_by_color.setter
    def get_by_color(self, value):
        self._by_color = [i for i in self.flowers if i.color == value]

    @property
    def get_by_length(self):
        return self._by_length

    @get_by_length.setter
    def get_by_length(self, value):
        self._by_length = [i for i in self.flowers if i.length == value]

    @property
    def get_by_cost(self):
        return self._by_cost

    @get_by_cost.setter
    def get_by_cost(self, value):
        self._by_cost = [i for i in self.flowers if i.cost == value]

    @property
    def get_by_name(self):
        return self._by_name

    @get_by_name.setter
    def get_by_name(self, value):
        self._by_name = [i for i in self.flowers if i.name == value]


flwrs = get_flowers_for_bouquet(random.randint(1, 15))
print(flwrs)
print(len(flwrs))

bouquet = Bouquet(flwrs)
print('bouquet_life_time')
print(bouquet.bouquet_life_time)
print('sort_by_cost')
print(bouquet.sort_by_cost)
print('sort_by_length')
print(bouquet.sort_by_length)
print('sort_by_color')
print(bouquet.sort_by_color)
print('sort_by_life_time')
print(bouquet.sort_by_life_time)
print('sort_by_name')
print(bouquet.sort_by_name)
print(bouquet.cost)
bouquet.get_by_life_time = 4
print(bouquet.get_by_life_time)
bouquet.get_by_color = "белый"
print(bouquet.get_by_color)
bouquet.get_by_cost = 220
print(bouquet.get_by_cost)
bouquet.get_by_length = 34
print(bouquet.get_by_length)
bouquet.get_by_name = "Роза"
print(bouquet.get_by_name)
