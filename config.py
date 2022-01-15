from zadacha3 import MoneyFmt
cash = MoneyFmt(12345678.021)
print(cash) #-- returns "$12,345,678.02"
cash.update(100000.4567)
print(cash) #-- returns "$100,000.46"
cash.update(-0.3)
print(cash) #-- returns "-$0.30"
repr(cash) #-- returns -0.3