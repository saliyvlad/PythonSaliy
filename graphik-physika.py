import matplotlib.pyplot as plt
import math

# Исходные данные
T1 = 3
T2 = 4
T = math.sqrt(T1**2 + T2**2)  # период нового маятника
theta0 = 0.1  # Амплитуда (в радианах)
duration = 10  # Время моделирования (в секундах)
num_points = 100  # Увеличиваем число точек для гладкости

# Расчет циклической частоты для нового маятника
omega = 2 * math.pi / T

# Создание массива времени
t = [duration * i / (num_points - 1) for i in range(num_points)]

# Вычисление угловых смещений только для нового маятника
theta = [theta0 * math.cos(omega * ti) for ti in t]

# Создание графика
plt.figure(figsize=(10, 6))
plt.plot(t, theta, label=f'Новый маятник (T={T:.2f} с)', linestyle='-', color='black')
plt.ylabel('Перемещение (рад)')  # Ось Y - перемещение
plt.title('Схематичный график колебаний нового маятника')


ax = plt.gca() # Получаем текущую систему координат
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(0.5)
ax.spines['left'].set_linewidth(0.5)
plt.tick_params(axis='both', which='both', length=0) # Убираем метки

plt.legend()


# Ось X - период с шагом T/4
x_ticks = []
x_labels = []
max_time = max(t)
for t_step in range(11):
  current_x_tick = t_step * T/4
  if current_x_tick <= max_time:
    x_ticks.append(current_x_tick)
    x_labels.append(f'{t_step}T/4')
plt.xticks(x_ticks, x_labels)  # Установка делений и подписей на оси X
plt.xlabel('Период колебаний')  # Ось X - период колебаний


# Ось Y - деления с шагом 0.02
min_y = min(theta)
max_y = max(theta)
y_ticks = [i * 0.02 for i in range(int(min_y / 0.02), int(max_y / 0.02) + 1)]
plt.yticks(y_ticks)

# Добавляем сетку
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.5)
plt.show()
