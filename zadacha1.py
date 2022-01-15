# 2
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь,
# из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома,
# общая площадь, оставшаяся площадь, список названий мебели.

class House:
    type = None
    area = 0
    def __init__(self, bedroom, garderob, chair):
        self.bedroom = bedroom
        self.garderob = garderob
        self.chair = chair
    def furniture (self, type, area):
        print("спальня",{self.bedroom}, "гардероб" ,{self.garderob},'стол',{self.chair})
        self.area = area
        self.type = type
        print('оставщаяся площадь', self.area - self.bedroom - self.chair - self.garderob)
        print('общая площадь',self.area)
        print('тип дома',self.type)
newHouse = House(4, 2, 1.5)
print(newHouse.__dict__)
newHouse.furniture("Особняк", 30)










