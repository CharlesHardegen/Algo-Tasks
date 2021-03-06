
'''
На числовой оси отмечен некоторый промежуток. 
Известно (вводится пользователем) 
начало этого промежутка a и его конец b. 
Промежуток разбивается на s равных частей
(также вводится пользователем). 
Необходимо в каждой точке промежутка вычислить синус и
косинус от координаты. 
Результаты вывести на консоль в виде ровной таблицы с заголовком
и разделителями.
'''

from math import sin, cos

# Вводить числа через пробел
a, b, c = map(int, input().split())
print('________________________________')
print('Координаты|    sin   |    cos   ')
print('    x    y|          |          ')
print('__________|__________|__________')

for i in range(min(a, b), max(a, b) + 1, c):
	print(f'{i:5d}{0:5d}|{sin(i):10.5f}|{cos(i):10.5f}')
