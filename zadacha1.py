# 2
# Furniture:
# Тип дома, общая площадь и перечень наименований мебели В новом доме совсем нет мебели.
# Мебель имеет название и площадь,
# из которых Спальня: 4 квадратных метра Гардероб: 2 квадратных метра Стол: 1,5 квадратных метра.
# Добавьте в дом три вышеупомянутых предмета мебели.
# При печати дома требуются следующие данные: тип дома,
# общая площадь, оставшаяся площадь, список названий мебели.

class Furniture:
    """Тип дома, общая площадь, мебели"""
    def __init__(self, bedroom = 4, wardrobe = 2, table = 1.5):
        self.bedroom = bedroom
        self.wardrobe = wardrobe
        self.table = table
        print("Дом состоит из следующих комнат в квадратных метрах")
        print('Спальня в кв/м ' + str(self.bedroom) +'\nГардероб в кв/м ' + str(self.wardrobe) + '\nСтол в кв/м ' + str(self.table))

house1= Furniture()
print(house1)




