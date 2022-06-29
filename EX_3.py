# задача про садовника и помидоры
class Tomato:

    # Стадии созревания помидора
    states = {0: 'nothing', 1: 'flower', 2: 'green_tomato', 3: 'red_tomato'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    # Переход к следующей стадии созревания
    def grow(self):
        self._change_state()

    # Проверка, созрел ли томат
    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    # Защищенные(protected) методы

    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def _print_state(self):
        print(f'Томат {self._index} - {Tomato.states[self._state]}')


class TomatoBush:

    # Создаем список из объектов класса Tomato
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]

    # Переводим все томаты из списка на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Проверяем, все ли помидоры созрели
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    # Собираем урожай
    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print('Садовник при деле ...')
        self._plant.grow_all()
        print('Садовник завязал')

    # Собираем урожай
    def harvest(self):
        print('Садовник собирает урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('Урожай собран, садовник хочет отдохнуть')
        else:
            print('Не надо торопиться, томаты еще не созрели')

    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''Убирать плоды надо в теплую погоду, когда на них нет капель влаги. 
        Лучше всего это делать утром, когда помидоры наиболее упругие и высококачественные. 
        Различают три степени зрелости плодов – зеленоспелые (побелевшие), бланжевые и спелые. 
        Зелёноспелые плоды уже достигли нормальных размеров и формы, их семена полностью сформированы. 
        Такие плоды при дозревании приобретают характерные для сорта вкус и окраску. 
        Не надо путать зеленоспелые (побелевшие) плоды, которые имеют зеленый цвет, 
        но полностью сформированы, и зеленые помидоры, которые находятся в стадии роста. 
        Эти плоды­подростки после снятия их с куста тоже постепенно дозревают, но они имеют совсем другой вкус. 
        А зеленоспелые плоды хороши для длительного хранения и перевозки на большие расстояния.''')


# Тесты
if __name__ == '__main__':
    Gardener.knowledge_base()
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Себастьян', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()