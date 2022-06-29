# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
def polindrom (word):
    if len(word) <= 1:  # если из 1 символа или пустота - полиндром
        return True
    f = word[::]
    b = word[::-1]
    if f == b:          # усли справа на лево = слева на право - полиндром
        return True
    elif f != b:
        return False
    return polindrom(word)

print(polindrom('dasad'))
