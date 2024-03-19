import numpy as np
from scipy.optimize import linprog

# Начальные данные
supply = [15, 23, 17, 32]
demand = [19, 21, 21, 18, 8]
costs = np.array([
    [6, 2, 4, 3, 15],
    [12, 10, 19, 8, 17],
    [2, 11, 14, 1, 14],
    [4, 7, 7, 12, 10]
])

# Преобразование задачи в задачу минимизации
c = costs.flatten()

# Ограничения на предложение и спрос
A_eq = []
for i in range(len(supply)):
    row = [0] * (len(supply) * len(demand))
    row[i * len(demand): (i + 1) * len(demand)] = [1] * len(demand)
    A_eq.append(row)
A_eq = np.array(A_eq)

b_eq = supply

A_ub = []
for j in range(len(demand)):
    row = [0] * (len(supply) * len(demand))
    for i in range(len(supply)):
        row[i * len(demand) + j] = 1
    A_ub.append(row)
A_ub = np.array(A_ub)

b_ub = demand

# Решение с помощью симплекс-метода
result = linprog(c, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, method='highs')

# Вывод результатов
print("Оптимальное решение:")
print(np.round(result.x.reshape(len(supply), len(demand)), decimals=2))
print("Суммарная стоимость перевозок:", np.round(result.fun, decimals=2))
