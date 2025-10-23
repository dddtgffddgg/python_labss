import ctypes
import numpy as np
import time

c_extension = ctypes.CDLL('./cyrashirenie.dll')

c_extension.N.argtypes = (ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int)
c_extension.N.restype = ctypes.c_double
c_extension.f.argtypes = (ctypes.c_double,)
c_extension.f.restype = ctypes.c_double
c_extension.g.argtypes = (ctypes.c_double,)
c_extension.g.restype = ctypes.c_double

def calculate_N(matrix):
    n, m = matrix.shape
    flattened_matrix = matrix.flatten()
    c_matrix = (ctypes.c_double * len(flattened_matrix))(*(flattened_matrix.tolist()))
    return c_extension.N(c_matrix, n, m)

def calculate_f(x):
    return c_extension.f(x)

def calculate_g(x):
    return c_extension.g(x)

matrix_size = 5_000
matrix = np.random.rand(matrix_size, matrix_size)

start_time = time.time()
result = calculate_N(matrix)
end_time = time.time()
execution_time = end_time - start_time
print("N(A) =", result)
print("Время выполнения N(A):", execution_time, "секунд")

x = 3.14
start_time = time.time()
result = calculate_f(x)
end_time = time.time()
execution_time = end_time - start_time
print("f(x) =", result)
print("Время выполнения f(x):", execution_time, "секунд")

x = 2.71
start_time = time.time()
result = calculate_g(x)
end_time = time.time()
execution_time = end_time - start_time
print("g(x) =", result)
print("Время выполнения g(x):", execution_time, "секунд")
