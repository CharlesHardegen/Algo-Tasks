
'''
В текстовом файле содержатся следующие данные: 
ширина N и высота M матрицы, 
а также данные самой матрицы в виде M строк по N символов в каждой. 
Строки состоят из символов «_» и «#». 
Из символов «#» составлен рисунок, размеры которого могут быть существенно 
меньше размеров всей матрицы (символами «_» обозначен фон). 
Необходимо запросить у пользователя два числа K и L — требуемые размеры матрицы, 
содержащей рисунок, при этом K>N и L>M. Необходимо найти рисунок на исходной 
матрице и увеличить его (и только его, незанятую рисунком часть фона не учитывать) 
до размеров KxL. Результат вывести в новый текстовый файл в виде матрицы размером KxL 
из символов «_» и «#»
'''

n, m = map(int, input().split())
input_image = [[input()] for i in range(m)]
binary_image = [[] for i in range(n)]

for i in range(n):
	for j in range(m):
		binary_image[i].append(1 if input_image[i][j] == "#" else 0)

print(binary_image)
