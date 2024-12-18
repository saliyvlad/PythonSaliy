
import matplotlib.pyplot as plt
import math

# Исходные данные
C = 2e-9
L = 0.15e-3
Um = 0.9
P = 1e-4

# Расчет параметров контура
w0 = 1 / math.sqrt(L * C)
T = 2 * math.pi / w0
W = 0.5 * C * Um**2
P_loss = P
delta_W = P_loss * T
delta = 0.5 * (delta_W / W)
beta = delta / T

# Моделирование затухающих колебаний
t_max = 10 * T
num_points = 15
t = [i * t_max / (num_points - 1) for i in range(num_points)]
A_t = [Um * math.exp(-beta * ti) for ti in t]

# Создание графика
plt.figure(figsize=(10, 6))
plt.plot(t, A_t, marker='*', linestyle='-', color='black')

# Настройка осей
plt.xlabel('Время (с)')
plt.ylabel('Амплитуда напряжения (В)')
plt.title('Схематичный график затухающих колебаний')

# Убираем контуры осей и метки
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.spines['left'].set_linewidth(0.5)
plt.tick_params(axis='both', which='both', length=0)

# Добавляем на ось Y значения, как в примере
plt.yticks([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])

# Добавляем метки для оси X - моменты времени T, 2T...
x_ticks = [i*T for i in range(11)]
x_labels = ['0'] + [f'{i}T' for i in range(1, 11)]
plt.xticks(x_ticks, x_labels)

# Добавляем сетку
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.5)


plt.show()

# Вывод логарифмического декремента
print(f"Логарифмический декремент затухания: {delta:.4f}")