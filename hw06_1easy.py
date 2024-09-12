print('{:*^30s}'.format('Задание-1:'))
# Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
#class
class Triangle:
    #атрибуты
    stXY = [0,0]
    ndXY = [10,0]
    rdXY = [10,10]
    #методы
    def get_a(self):
        return round(((self.ndXY[0] - self.stXY[0]) ** 2 + (self.ndXY[1] - self.stXY[1]) ** 2) ** 0.5, 2)
    def get_b(self):
        return round(((self.rdXY[0] - self.stXY[0]) ** 2 + (self.rdXY[1] - self.stXY[1]) ** 2) ** 0.5, 2)
    def get_c(self):
        return round(((self.rdXY[0] - self.ndXY[0]) ** 2 + (self.rdXY[1] - self.ndXY[1]) ** 2) ** 0.5, 2)
    def get_perimeter (self):
        return round((self.get_a() + self.get_b() + self.get_c()), 2)
    def get_square (self):
        return round((self.get_perimeter()/2 * (self.get_perimeter() / 2 - self.get_a()) * (self.get_perimeter() / 2 - self.get_b()) * (self.get_perimeter() / 2 - self.get_c())) ** 0.5, 2)
    def get_h(self):
        return round((2 * self.get_square()) / self.get_a(), 2)

trang = Triangle()
print('a = ', trang.get_a())
print('b = ', trang.get_b())
print('c = ', trang.get_c())
print('Периметр = ', trang.get_perimeter())
print('Площадь треугольника = ', trang.get_square())
print('высота треугольника к стороне |а| = ', trang.get_h())


print('{:*^30s}'.format('Задание-2:'))
# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
#class
class Trapezium:
    #атрибуты
    stXY = [0,0]
    ndXY = [30,0]
    rdXY = [5,10]
    rtXY = [25,10]
    #методы
    def get_a(self):
        return round(((self.ndXY[0] - self.stXY[0]) ** 2 + (self.ndXY[1] - self.stXY[1]) ** 2) ** 0.5, 2)
    def get_b(self):
        return round(((self.rdXY[0] - self.stXY[0]) ** 2 + (self.rdXY[1] - self.stXY[1]) ** 2) ** 0.5, 2)
    def get_c(self):
        return round(((self.rtXY[0] - self.rdXY[0]) ** 2 + (self.rtXY[1] - self.rdXY[1]) ** 2) ** 0.5, 2)
    def get_d(self):
        return round(((self.rtXY[0] - self.ndXY[0]) ** 2 + (self.rtXY[1] - self.ndXY[1]) ** 2) ** 0.5, 2)
    def iso_trap(self):
        if self.get_d() == self.get_b() and self.get_a() != self.get_c():
            print('Tрапеция РАВНОбедренная')
        else:
            print('Трапеция НЕ-РАВНОбедренная')
    def get_perimeter (self):
        return round((self.get_a() + self.get_b() + self.get_c() + self.get_d()), 2)
    def get_square (self):
        return round((((self.get_a() + self.get_c()) / 4) * ((4 * self.get_b() ** 2) - (self.get_a() - self.get_c()) ** 2) ** 0.5), 1)

print('''
     A3_______c__________A4
      /                  \\
    b/                    \\d
    /                      \\
   /                        \\
  /__________________________\\
 A1         a                 A2''')
trpz = Trapezium()
print('a = ', trpz.get_a())
print('b = ', trpz.get_b())
print('c = ', trpz.get_c())
print('d = ', trpz.get_d())
trpz.iso_trap()
print('Периметр = ', trpz.get_perimeter())
print('Площадь трапеции = ', trpz.get_square())


