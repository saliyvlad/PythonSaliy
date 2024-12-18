import matplotlib.pyplot as plt
import math

def calculate_displacement(time, period, amplitude):
    """
    Вычисляет смещение маятника в заданный момент времени.

    Args:
        time (float): Время (секунды).
        period (float): Период колебаний (секунды).
        amplitude (float): Амплитуда колебаний (произвольные единицы).
    
    Returns:
        float: Смещение маятника.
    """

    angular_frequency = 2 * math.pi / period
    displacement = amplitude * math.cos(angular_frequency * time)
    return displacement

def plot_pendulum_motion(T1, T2, T3, amplitude=10, duration=20, num_points=500):
    """
    Строит графики колебаний трех математических маятников.

    Args:
        T1 (float): Период первого маятника (секунды).
        T2 (float): Период второго маятника (секунды).
        T3 (float): Период третьего маятника (секунды).
        amplitude (float): Амплитуда колебаний (в произвольных единицах).
        duration (float): Длительность отображаемого времени (секунды).
        num_points (int): Количество точек для построения графика.
    """

    t_values = [duration * i / num_points for i in range(num_points)] # Создаем временную шкалу
    x1_values = [calculate_displacement(t, T1, amplitude) for t in t_values]
    x2_values = [calculate_displacement(t, T2, amplitude) for t in t_values]
    x3_values = [calculate_displacement(t, T3, amplitude) for t in t_values]

    # Создание графиков
    plt.figure(figsize=(10, 6))

    plt.plot(t_values, x1_values, label=f'Маятник 1 (T={T1} с)')
    plt.plot(t_values, x2_values, label=f'Маятник 2 (T={T2} с)')
    plt.plot(t_values, x3_values, label=f'Маятник 3 (T={T3} с)')

    plt.xlabel('Время (с)')
    plt.ylabel('Смещение (произвольные единицы)')
    plt.title('Колебания математических маятников')
    plt.legend()
    plt.grid(True)
    plt.show()


# Заданные периоды
T1 = 3
T2 = 4
T3 = 5  # Вычисляется из условия задачи

plot_pendulum_motion(T1, T2, T3)
