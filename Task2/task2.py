import sys

# Функция для проверки положения точки относительно окружности
def check_position(circle_center, radius, point):
    distance = ((point[0] - circle_center[0]) ** 2 + (point[1] - circle_center[1]) ** 2) ** 0.5
    if distance == radius:
        return 0  # Точка лежит на окружности
    elif distance < radius:
        return 1  # Точка внутри окружности
    else:
        return 2  # Точка снаружи окружности

# Считывание координат и радиуса окружности из файла
circle_file = sys.argv[1]
with open(circle_file, 'r') as file:
    circle_center = list(map(float, file.readline().split()))
    radius = float(file.readline())

# Считывание координат точек из файла
points_file = sys.argv[2]
with open(points_file, 'r') as file:
    points = [list(map(float, line.split())) for line in file]

# Проверка положения каждой точки относительно окружности и вывод результата
for point in points:
    position = check_position(circle_center, radius, point)
    print(position)