#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <locale.h>

double f(int x) {
    return sin(x) - pow(cos(x), 1.5);
}

double g(int x) {
    return x * x - 1 / tan(x / 99.0 + 0.01);
}

int** calculate_matrix(int rows, int cols) {
    int** matrix = (int**)malloc(rows * sizeof(int*));

    for (int i = 0; i < rows; i++) {
        matrix[i] = (int*)malloc(cols * sizeof(int));
        for (int j = 0; j < cols; j++) {
            matrix[i][j] = (int)(f(i + 1) + g(j + 1));
        }
    }

    return matrix;
}

int find_max_column_sum(int** matrix, int rows, int cols) {
    int max_sum = -1;

    for (int j = 0; j < cols; j++) {
        int column_sum = 0;
        for (int i = 0; i < rows; i++) {
            column_sum += abs(matrix[i][j]);
        }
        if (column_sum > max_sum) {
            max_sum = column_sum;
        }
    }

    return max_sum;
}

int main() {
    setlocale(LC_ALL, "en_US.UTF-8"); // Используем кодировку UTF-8

    int dimensions[] = { 10, 50, 100, 500, 1000, 1500, 5000 };
    int num_dimensions = sizeof(dimensions) / sizeof(dimensions[0]);

    for (int i = 0; i < num_dimensions; i++) {
        int dimension = dimensions[i];

        int** matrix = calculate_matrix(dimension, dimension);

        clock_t start_time = clock();

        int max_column_sum = find_max_column_sum(matrix, dimension, dimension);

        clock_t end_time = clock();
        double execution_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;

        printf("Размерность матрицы: %dx%d\n", dimension, dimension);
        printf("Время выполнения: %.6f секунд\n", execution_time);
        printf("\n");

        for (int j = 0; j < dimension; j++) {
            free(matrix[j]);
        }
        free(matrix);
    }

    return 0;
}
