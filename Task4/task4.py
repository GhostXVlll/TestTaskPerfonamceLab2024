import sys

# Чтение массива из файла
with open(sys.argv[1], 'r') as file:
    nums = [int(line) for line in file]

# Вычисление минимального и максимального значения в массиве
min_num = min(nums)
max_num = max(nums)

# Вычисление минимального количества ходов
min_moves = float('inf')
for target in range(min_num, max_num+1):
    moves = sum(abs(num - target) for num in nums)
    min_moves = min(min_moves, moves)

# Вывод результата
print(min_moves)
