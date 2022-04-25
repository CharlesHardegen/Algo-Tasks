
'''
Запросить у пользователя координаты вершин треугольника. 
Вычислить длину вписанной в этот треугольник окружности 
и площадь круга. 
Вывести результаты на консоль
'''

from math import sqrt

sides_l = []
cords = []
for i in range(3):
	x, y = map(int, input().split())
	cords.append([x, y])

sides_l.append(sqrt((cords[0][0] - cords[1][0])**2 \
	+ (cords[0][1] - cords[1][1])**2))
sides_l.append(sqrt((cords[1][0] - cords[2][0])**2 \
	+ (cords[1][1] - cords[2][1])**2))
sides_l.append(sqrt((cords[2][0] - cords[0][0])**2 \
	+ (cords[2][1] - cords[0][1])**2))

p = sides_l[0] + sides_l[1] + sides_l[2]
p2 = p / 2
s = sqrt(p2 * (p2 - sides_l[0]) * \
	(p2 - sides_l[1]) * (p2 - sides_l[2]))

r = s / p2

print(2 * 3.14 * r, 3.14 * r * r)
