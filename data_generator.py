import numpy as np
import random

def save_matrix(dimension: int = 5) -> None:
    matrix = generate_tsp_matrix(dimension)
    np.savetxt(f"datasets/{dimension}.txt", matrix, fmt='%d')

def generate_tsp_matrix(num_cities: int) -> np.ndarray:
    matrix = np.random.randint(1, 100, size=(num_cities, num_cities))
    matrix = (matrix + matrix.T) / 2
    np.fill_diagonal(matrix, 0)
    return matrix

if __name__ == "__main__":
    for i in range(5, 21):
        save_matrix(i)