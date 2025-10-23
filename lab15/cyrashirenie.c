#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif

EXPORT double N(double* matrix, int rows, int cols) {
    double max_sum = -1;

    for (int j = 0; j < cols; j++) {
        double column_sum = 0;
        for (int i = 0; i < rows; i++) {
            column_sum += fabs(matrix[i * cols + j]);
        }
        if (column_sum > max_sum) {
            max_sum = column_sum;
        }
    }

    return max_sum;
}

EXPORT double f(double x) {
    return sin(x) - cos(pow(x, 1.5));
}

EXPORT double g(double x) {
    return pow(x, 2) - (1 / tan(x / 99.0 + 0.01));
}

EXPORT void calculate_matrix(double* matrix, int rows, int cols) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            matrix[i * cols + j] = f(i + 1) + g(j + 1);
        }
    }
}
