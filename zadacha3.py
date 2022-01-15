#  4
# Dollar
# Создайте функцию dollarize (), которая принимает Float и возвращает долларовый формат:
#
# Copy
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"
#
# Преобразуйте эту функцию в полезный класс MoneyFmt. MoneyFmt содержит одно значение данных (количество) и 4 метода.
# Copy
#     "init" //конструктор инициализирует значение данных
#     "update" //метод заменяет значение данных новым
#     "repr" //методы возвращают значение с плавающей запятой
#     "str" //метод, реализующий логику метода dollarize ()
#
# Copy
# //Результат будет выглядеть так:
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3
#
# import moneyfmt
# cash = moneyfmt.MoneyFmt(12345678.021)
# print(cash) -- returns "$12,345,678.02"
# cash.update(100000.4567)
# print(cash) -- returns "$100,000.46"
# cash.update(-0.3)
# print(cash) -- returns "-$0.30"
# repr(cash) -- returns -0.3

# def dollarize(dollar):
#     return '${:,.2f}'.format(dollar)

# print(dollarize(123456.78901))
# dollarize(-123456.7801)
# dollarize(1000000)

class MoneyFmt:
    def __init__(self, kol):
        self.kol = kol

    def update(self, kol_new):
        self.kol = kol_new

    def __repr__(self):
        return f"${round(self.kol, 1)}"

    def __str__(self):
        g = round(self.kol, 2)
        return f'${g}'


