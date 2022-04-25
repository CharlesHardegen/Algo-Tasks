
from collections import deque

def print_field(field, path):
	def splitted(s):
		return [char for char in s]

	output_field = []
	for i in range(len(field)):
		output_field.append(splitted(field[i]))

	for i in path:
		output_field[i[0]][i[1]] = 'P'

	for i in range(len(output_field)):
		for j in range(len(output_field[i])):
			print(output_field[i][j], end='')
		print()

def bfs(field, s, t):
	n = len(field)
	m = len(field[0])
	INF = 10 ** 9 #inf max num
	delta = [(0, -1), (0, 1), (1, 0), (-1, 0)]
	d = [[INF] * m for _ in range(n)]
	p = [[None] * m for _ in range(n)]
	used = [[False] * m for _ in range(n)]
	queue = deque()

	d[s[0]][s[1]] = 0
	used[s[0]][s[1]] = True
	queue.append(s)

	while len(queue) != 0:
		x, y = queue.popleft()
		for dx, dy in delta:
			nx, ny = x + dx, y + dy
			if 0 < nx < n and 0 < ny < m and not used[nx][ny] and field[nx][ny] != "#":
				d[nx][ny] = d[x][y] + 1
				p[nx][ny] = (x, y)
				used[nx][ny] = True
				queue.append((nx, ny)) 
	print(d[t[0]][t[1]])
	cur = t
	path = []
	while cur is not None:
		path.append(cur)
		cur	= p[cur[0]][cur[1]]
	path.reverse()
	print_field(field, path)

if __name__ == '__main__':
	fin = open('input.txt', 'r')
	field = fin.readlines()
	s = list(map(int, field[1].strip().split()))
	t = list(map(int, field[2].strip().split()))
	field.pop(0)
	field.pop(0)
	field.pop(0)
	n = len(field)
	m = len(field[0]) - 1
	for i in range(n):
		field[i] = field[i].strip()

	bfs(field, s, t)
