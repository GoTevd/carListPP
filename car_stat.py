# Сделаем программу, которая будет анализировать пробег и возраст автомобиля и предлагать различные
# услуги. К примеру, если пробег автомобиля более 100000км. или автомобилю уже более 3-ёх
# лет, то в комментариях выводится рекомендация.


class Car:
# создаём класс


  def __init__(self, brand, model, age, odometer, engine_cc, gear_box):
# инициализируем данные автомобиля
    self.brand = brand
    self.model = model
    self.age = age
    self.odometer = odometer
    self.engine_cc = engine_cc
    self.gear_box = gear_box


# теперь нужно продумать условия и сделать так, чтобы все комментарии проходили
# для определения возраста автомобиля можно использовать следующий скрипт или класс
# или функция или модуль
# from datetime import date
# date_of_manufacture = int(input())
# today = date.today()
# print(today.year - date_of_manufacture)


# для нумерации списка можно использовать вот такой код
# items = ['молоко', 'сыр', 'творог', 'кефир', 'яблоко']
# for i, item in enumerate(items):
#   print(str(i + 1) + '. ' + item, sep='')


  def odo(self):
# метод для определения технической инспекции
    if self.odometer > 100000:
      return ('Car need tech inspection.')
    else:
      return ('Car is OK.')



  def information(self):
# описание автомобиля, вывод
    info = self.brand + ' ' + self.model + ' ' + str(self.age) + ' ' + str(self.odometer) + ' ' + str(self.engine_cc) + ' ' + self.gear_box + ' ' + self.odo()
    return info.title()


car_test1 = Car('volkswagen', 'golf', 9, 187000, 1399, 'A')
car_test2 = Car('volkswagen', 'tiguan', 5, 64000, 1998, 'A')
car_test3 = Car('audi', 'a3', 2, 34000, 1799, 'm')
car_test4 = Car('skoda', 'oktavia', 10, 57000, 1399, 'A')
car_test5 = Car('audi', 'a5', 7, 58000, 3969, 'm')
print(car_test1.information())
print(car_test2.information())
print(car_test3.information())
print(car_test4.information())
print(car_test5.information())
