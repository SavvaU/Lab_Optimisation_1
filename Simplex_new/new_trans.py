import numpy as np
from new_simplex import simplex

def read_input_data(filename: str):
    """
    Считывание входных данных из файла.

    :param filename: Имя файла с входными данными.
    :return: Кортеж с данными транспортной задачи.
    """
    try:
        with open(filename, 'r') as fp:
            # Считываем предложения
            supply_list = list(map(int, fp.readline().split()))
            # Считываем спрос
            demand_list = list(map(int, fp.readline().split()))

            # Считываем матрицу стоимостей перевозок
            costs_matrix = [list(map(int, line.split())) for line in fp if not (line.startswith('N') or line.startswith('Y'))]

            A = np.zeros((len(supply_list) + len(demand_list),(len(supply_list) * len(demand_list))))
            for i in range(len(supply_list)):
                for j in range(len(demand_list)):
                    A[i][j + i * len(demand_list)] = 1
            for i in range(len(demand_list)):
                for j in range(len(supply_list)):
                    A[i + len(supply_list)][j * (len(demand_list)) + i] = 1
            z = [-1 *  element for row in costs_matrix for element in row]
            b = supply_list + demand_list
            return z, A, b
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return [], [], [], [], []


z, A, b = read_input_data("trans.txt")
simplex(z, A.tolist(), b)