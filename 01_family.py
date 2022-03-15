# -*- coding: utf-8 -*-
from termcolor import cprint
from random import randint
import random


# =============================================== Часть первая==============================================
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.

# Выделить базовый класс для мужа и жены


class House:
    def __init__(self):
        self.food = 50  # еда
        self.cat_food = 30  # еда для кота
        self.money = 100
        self.mud = 0  # грязь
        self.total_money = 0  # всего потрачено денег
        self.total_food = 0
        self.total_food_cat = 0

    def __str__(self):
        self.mud += 5
        return f'В доме еды осталось  = {int(self.food)}: Денег осталось = {int(self.money)}:' \
               f' Еды для кота осталось =  {self.cat_food} :Грязи в доме накопилось {self.mud} '


class Human:
    def __init__(self, name, message_color, eaten, died):
        self.satiety = 30  # сытость

        self.happiness = 100  # счастье
        self.ate_food = 0  # съели еды

        self.all_champagne = 0  # всего шампанского
        self.home = home
        self.name = name
        self.message_color = message_color
        self.eaten = eaten  # съел или съела
        self.died = died  # умер или умерла

    def act(self):
        if self.satiety < 0:
            cprint('{} {} от голода... '.format(self.name, self.died),
                   color=self.message_color)
            self.satiety = 0  # сытость
            self.happiness = 0  # счастье
            self.ate_food = 0  # съедено еды
            return

        if self.happiness < 10:
            cprint('{} {} от дипрессии...'.format(self.name, self.died), color=self.message_color)
            self.satiety = 0  # сытость
            self.happiness = 0  # счастье
            self.ate_food = 0  # съел еды
            return

        if self.satiety <= 20:
            if self.home.food > 10:
                self.eat()
        else:
            self.ate_food = 0

        if self.home.mud > 90:
            self.happiness -= 10

        if self.satiety > 20:
            self.pet_the_cat()  # гладит кота

        return True

    def eat(self):
        if self.home.food > 30:
            cprint(f'{self.name} ест', color=self.message_color)
            self.ate_food = random.randint(20, 29)
            self.home.food -= self.ate_food
            self.satiety += self.ate_food

        else:
            cprint(f'{self.name} ест', color=self.message_color)
            self.ate_food = random.randint(10, 15)
            self.home.food -= self.ate_food
            self.satiety += self.ate_food
            cprint(f'Еды осталось {self.home.food}', color=self.message_color)

        # else:
        #     cprint(f'Еды осталось {self.home.food}', color=self.message_color)

    def pet_the_cat(self):  # гладит кота
        cprint(f'{self.name} гладит кота', color=self.message_color)
        self.satiety -= 10
        self.happiness += 5

    def __str__(self):
        super().__str__()
        return '{} - {} еды = {}: Cытость = {}: Коффициент счастья = {}' \
            .format(self.name, self.eaten, self.ate_food, self.satiety, self.happiness)


class Husband(Human):
    def __init__(self, name):
        super().__init__(name, message_color='yellow', eaten='съел', died='умер')
        self.name = name
        self.home = home
        self.masha = masha
        self.message_color = 'yellow'
        self.eaten = 'съел'
        self.died = 'умер'

    def act(self):
        if super().act():

            if self.satiety > 30:
                self.roll_a_dice()
            else:
                self.eat()

            if self.masha.happiness <= 20:
                cprint(f'У {self.masha.name} началась депрессия. Пусть {self.name}  даст деньги на  шампанское',
                       color='red')
                self.masha.buying_champagne()

            if self.home.money <= 150:
                self.work()

    def work(self):
        if self.satiety > 10:
            cprint(f'{self.name} идет работать', color=self.message_color)
            self.satiety -= 10
            self.home.money += 150
            self.home.total_money += 150
        else:
            cprint(f'У {self.name} нет сил работать', color=self.message_color)
            self.eat()

    def roll_a_dice(self):
        cprint(f'{self.name} кидает кубик - играть или смотреть ТВ', color=self.message_color)
        throw = randint(1, 4)
        self.satiety -= 10  # сытость уменьшается
        if throw == 1 or throw == 2 or throw == 3:
            cprint(f'{self.name} идет играть в WoT', color=self.message_color)
            self.gaming()
        else:
            self.eat()
        if throw == 2:
            if self.satiety >= 10:
                cprint(f'{self.name} идет смотреть  ТВ', color=self.message_color)
                self.satiety -= 10  # сытость уменьшается

            else:
                cprint(f'У {self.name} нет сил смотреть ТВ', color=self.message_color)
                self.eat()

    def gaming(self):
        if self.satiety >= 10:
            self.satiety -= 10
            played = randint(1, 3)
            if played == 1 or played == 2:
                cprint(f'{self.name} проиграл', color='red')
                self.happiness -= 20

            else:
                win = ['Ура ! Я выиграл! Иди жена за шубой!', 'Ура ! Я выиграл! Иди жена за шампанским']
                cprint(f'{self.name} выиграл!', color=self.message_color)
                self.happiness += 20
                res = random.choice(win)
                if res == 'Ура ! Я выиграл! Иди жена за шубой!':
                    cprint('Ура ! Я выиграл! Иди жена за шубой!', color=self.message_color)
                    self.masha.buy_fur_coat()
                    if self.home.money < 400:
                        self.work()

                if res == 'Ура ! Я выиграл! Иди жена за шампанским':
                    cprint('Ура ! Я выиграл! Иди жена за шампанским', color=self.message_color)
                    self.masha.buying_champagne()
                    if self.home.money < 100:
                        self.work()
        else:
            cprint(f'У {self.name} нет сил играть', color='red')


class Wife(Human):

    def __init__(self, name):
        super().__init__(name, message_color='blue', eaten='съела', died='умерла')
        self.name = name
        self.home = home
        self.cleaning = 0
        self.buy_products = 0  # купила продуктов
        self.buy_products_cat = 0  # купила еды коту
        self.total_fur_coats = 0  # всего шуб
        self.message_color = 'blue'
        self.eaten = 'съела'
        self.died = 'умерла'

    def act(self):
        if super().act():

            if self.home.money >= 500:
                cprint(f'{self.name} накопила деньги на шубу', self.message_color)
                self.buy_fur_coat()

            if self.home.food <= 50:
                self.shopping()
            else:
                self.buy_products = 0

            if self.home.cat_food < 30:
                self.shopping_cat()
            else:
                self.buy_products = 0

            if self.home.mud >= 100:
                self.clean_house()

    def shopping(self):
        if self.home.money > 30:
            if self.satiety > 10:
                print('Сколько денег осталось до похода в магазин', self.home.money)
                cprint(f'{self.name} идет за продуктами в магазин', self.message_color)
                self.buy_products = 0
                self.buy_products += int(self.home.money * 0.3)  # покупаем еду
                cprint(f'{self.name} купила продуктов = {self.buy_products}', self.message_color)
                self.home.food += self.buy_products
                self.home.money -= self.buy_products
                self.satiety -= 10
                self.home.total_food += self.buy_products
            else:
                self.eat()

        if self.home.money < 30:
            if self.satiety >= 10:
                print('Сколько денег осталось до похода в магазин', self.home.money)
                cprint(f'{self.name} идет за продуктами в магазин', self.message_color)
                self.buy_products = 0
                self.buy_products += int(self.home.money * 0.5)
                cprint(f'{self.name} купила продуктов = {self.buy_products}', self.message_color)
                self.home.food += int(self.buy_products)
                self.home.money -= int(self.buy_products)
                self.satiety -= 10
                self.home.total_food += self.buy_products

    def shopping_cat(self):
        if self.home.money > 20:
            if self.satiety > 10:
                print('Сколько денег в кошельке', self.home.money)
                cprint(f'{self.name} идет за едой коту', self.message_color)
                self.buy_products_cat = 0
                self.buy_products_cat += random.randint(20, 31)  # покупка еды коту
                cprint(f'{self.name} купила продуктов коту = {self.buy_products_cat}', self.message_color)
                self.home.cat_food += self.buy_products_cat
                self.satiety -= 10
                self.home.total_food_cat += self.buy_products_cat
            if self.satiety < 10:
                self.eat()

    def buy_fur_coat(self):  # покупка шубы
        if self.satiety >= 20:
            if self.home.money >= 400:
                cprint(f'{self.name} счастливая идет за шубой', self.message_color)
                self.home.money -= 350
                self.happiness += 60
                self.satiety -= 10
                self.total_fur_coats += 1
            else:
                cprint(f'{self.name} нехватает денег на  шубу', self.message_color)

    def buying_champagne(self):
        if self.satiety >= 20:
            if self.home.money > 100:
                cprint(f'{self.name} идет за шампанским', self.message_color)
                self.home.money -= 50
                self.happiness += 20
                self.satiety -= 10
                self.all_champagne += 1
            else:
                cprint(f'{self.name} нехватает денег на  шампанское', self.message_color)

        else:
            self.eat()

    def clean_house(self):
        if self.satiety >= 10:
            cprint(f'{self.name} уборка в доме', self.message_color)
            self.satiety -= 10
            self.cleaning = random.randint(90, 101)  # уборка рандом
            self.home.mud -= self.cleaning


class Cat:
    # Cделать коту что бы он подкидывал монеты - драть обои или спать
    def __init__(self, name):
        self.name = name
        self.home = home
        self.satiety_cat = 30  # сытость кота
        self.cat_ate_food = 0  # кот съел еды
        self.message_color = 'grey'

    def __str__(self):

        return '{} - съел еды = {}: Cытость = {}' \
            .format(self.name, self.cat_ate_food, self.satiety_cat)

    def act(self):
        if self.satiety_cat < 0:
            cprint(f'{self.name}  умер от голода... ', color='red')
            self.satiety_cat = 0  # сытость
            self.cat_ate_food = 0  # съедено еды

        if self.satiety_cat <= 20:
            self.eat()

        if self.satiety_cat > 20:
            self.flips_a_coin()  # подбрасывает монету

    def eat(self):
        if self.home.cat_food > 10:
            cprint(f'{self.name} ест', color=self.message_color)
            self.cat_ate_food = random.randint(5, 11)  # съел еды
            self.home.cat_food -= self.cat_ate_food  # еда уменьшилась
            self.satiety_cat += self.cat_ate_food  # сытость добавилась
        else:
            cprint(f'{self.name} хочет есть, а еды нет', color='red')

    def flips_a_coin(self):  # подбрасывает монету
        cprint(f'{self.name} подбрасывает монету - спать или драть обои', color=self.message_color)
        res = random.randint(1, 2)
        if res == 1:
            self.soil()

        if res == 2:
            self.sleep()

        self.satiety_cat -= 10

    def sleep(self):
        cprint(f'{self.name} спит', color=self.message_color)
        self.satiety_cat -= 10

    def soil(self):  # дерет обои
        cprint(f'{self.name} дерет обои', color=self.message_color)
        self.satiety_cat -= 10
        self.home.mud += 5


# ================================================== Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#     Зделать коту что бы он подкидывал монеты - драть обои или спать
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


# ===========================================================Часть вторая бис========================================
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Human):

    def __init__(self, name):
        super().__init__(name, message_color='yellow', eaten='съел', died='умер')
        self.name = name
        self.home = home
        self.masha = masha
        self.message_color = 'cyan'
        self.eaten = 'съел'
        self.died = 'сильно плачет'

    def act(self):
        if self.satiety > 10:
            self.sleep()
            self.ate_food = 0

        else:
            self.eat()

    def eat(self):
        if self.home.food > 30:
            cprint(f'{self.name} ест', color=self.message_color)
            self.ate_food = random.randint(5, 10)
            self.home.food -= self.ate_food
            self.satiety += self.ate_food

    def sleep(self):
        cprint(f'{self.name} спит', self.message_color)
        self.satiety -= 10


# ================================================Часть третья=====================================================
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.

home = House()
masha = Wife(name='Маша')
serge = Husband(name='Сережа')
cat = Cat(name='Базилио')
gosha = Child(name='Гоша')

for day in range(1, 1000):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    cat.act()
    gosha.act()
    cprint(serge, color='magenta')
    cprint(masha, color='magenta')
    cprint(cat, color='magenta')
    cprint(gosha, color='magenta')
    cprint(home, color='yellow')
print('=' * 80)
print('Всего заработано денег = ', home.total_money)
print('Всего куплено еды = ', home.total_food)
print('Всего куплено еды коту = ', home.total_food_cat)
print('Всего куплено шуб = ', masha.total_fur_coats)
print('Выпито бутылок шампанского', masha.all_champagne)

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

# Зачёт!
