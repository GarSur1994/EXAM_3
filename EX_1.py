# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками
def credit(card):
    return '*' * len(str(card[:-4])) + str(card[-4:])

print(credit('341234267125358'))