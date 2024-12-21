import matplotlib.pyplot as plt
import math
import numpy as np

# Исходные данные
T = 3.44e-6  # Период колебаний
delta = 0.2124  # Логарифмический декремент
Um = 0.9  # Начальная амплитуда напряжения
beta = delta / T  # Коэффициент затухания
omega0 = 2 * math.pi / T  # Циклическая частота

duration = 10 * T # Время моделирования (10 периодов)
num_points = 500 # Увеличиваем точки для гладкости

# Создание массива времени
t = np.linspace(0, duration, num_points)

# Вычисление напряжения на конденсаторе
U = Um * np.exp(-beta * t) * np.cos(omega0 * t)
U0 = Um * np.exp(-beta * t)

# Создание графика
plt.figure(figsize=(10, 6))
plt.plot(t, U, linestyle='-',label=f'(График затухающих колебаний', color='green')
plt.plot(t, U0, linestyle='--',label=f'(График амплитуды затухания)', color='black')
plt.plot(t, -U0, linestyle='--',label=f'(График амплитуды затухания)', color='black')
plt.xlabel('Время (с)')
plt.ylabel('Напряжение (В)')
plt.title('Затухающие колебания напряжения')
plt.grid(True, linestyle='--', linewidth=0.5, color='gray', alpha=0.5)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.spines['left'].set_linewidth(0.5)
plt.legend()
plt.tick_params(axis='both', which='both', length=0)

plt.show()
