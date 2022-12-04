def f(x):
    return x // 10, x % 10  # возвращает tuple


# lambda x: (возвращаем элементы) - нужна лямбда для прохождения по каждому элементу - тоже самое как f(x)
# чтобы число было в обратном порядке нужно написать переж числом минус или сделать так чтобы большее значение - стало меньшим

def fX(x):
    return x // 10


def getNumber(x):
    return int(x.split()[1])


def getLower(x):
    return x.split()[0].lower()


a = ['ZZZ 800', 'aaa 45', 'eee 43', 'ddd 800', 'AaA 43', 'aaa 14']
a = sorted(a, key=lambda x: getNumber(x), reverse=True)
a = sorted(a, key=lambda x: getLower(x), reverse=True)
print(a)
