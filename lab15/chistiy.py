import random
import time
import math

def f(x):
    return math.sin(x) - math.cos(x) ** 1.5

def g(x):
    return x * x - 1 / math.tan(x/99 + 0.01)

def calculate_matrix(rows, cols):
    matrix = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = f(i+1) + g(j+1)

    return matrix

def find_max_column_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    max_sum = -1

    for j in range(cols):
        column_sum = 0
        for i in range(rows):
            column_sum += abs(matrix[i][j])
        if column_sum > max_sum:
            max_sum = column_sum

    return max_sum

dimensions = [10, 50, 100, 500, 1000, 1500, 5000]

for dimension in dimensions:
    matrix = calculate_matrix(dimension, dimension)

    start_time = time.time()

    max_column_sum = find_max_column_sum(matrix)

    end_time = time.time()
    execution_time = end_time - start_time

    print("Размерность матрицы: {} x {}".format(dimension, dimension))
    print("Время выполнения:", execution_time, "секунд")
    print()
