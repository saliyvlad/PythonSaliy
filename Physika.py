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







import matplotlib.pyplot as plt
import math

def calculate_damped_oscillation(time, amplitude, frequency, damping_coefficient):
    """
    Вычисляет напряжение в контуре с затухающими колебаниями.

    Args:
        time (float): Время (секунды).
        amplitude (float): Начальная амплитуда напряжения (вольты).
        frequency (float): Частота колебаний (Гц).
        damping_coefficient (float): Коэффициент затухания.

    Returns:
        float: Напряжение в контуре.
    """

    angular_frequency = 2 * math.pi * frequency
    voltage = amplitude * math.exp(-damping_coefficient * time) * math.cos(angular_frequency * time)
    return voltage

def plot_damped_oscillation(amplitude, frequency, damping_coefficient, duration=0.000005, num_points=500):
    """
    Строит график затухающих колебаний.

    Args:
        amplitude (float): Начальная амплитуда напряжения (вольты).
        frequency (float): Частота колебаний (Гц).
        damping_coefficient (float): Коэффициент затухания.
        duration (float): Длительность отображаемого времени (секунды).
        num_points (int): Количество точек для построения графика.
    """

    t_values = [duration * i / num_points for i in range(num_points)]
    u_values = [calculate_damped_oscillation(t, amplitude, frequency, damping_coefficient) for t in t_values]

    # Создание графика
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, u_values)

    plt.xlabel('Время (с)')
    plt.ylabel('Напряжение (В)')
    plt.title('Затухающие колебания в контуре')
    plt.grid(True)
    plt.show()

# Заданные параметры
C = 2e-9  # Ф
L = 0.15e-3  # Гн
Um = 0.9  # В
P = 1e-4  # Вт

# Расчет частоты
omega = 1 / math.sqrt(L * C)
frequency = omega / (2 * math.pi)

# Расчет сопротивления
R = Um**2 / (2 * P)

# Расчет добротности
Q = (omega * L) / R

# Расчет коэффициента затухания
damping_coefficient = omega / (2 * Q)

plot_damped_oscillation(Um, frequency, damping_coefficient)
Объяснение кода:

Импорт библиотек:
matplotlib.pyplot (plt): Для построения графиков.
math: Для математических функций.
Функция calculate_damped_oscillation:
Принимает время, начальную амплитуду, частоту и коэффициент затухания.
Вычисляет напряжение в контуре с затухающими колебаниями, используя экспоненциальную функцию для затухания и косинус для колебаний.
Функция plot_damped_oscillation:
Принимает амплитуду, частоту, коэффициент затухания, продолжительность времени и количество точек.
Создаёт массив времени t_values используя list comprehension.
Создаёт массив напряжений u_values для каждого момента времени, используя функцию calculate_damped_oscillation.
Создаёт область для графика и строит график с помощью plt.plot.
Настраивает оси, заголовок и сетку.
plt.show() показывает график.
Расчет параметров:
Задаём параметры контура: C, L, Um, P.
Вычисляем циклическую частоту omega, частоту frequency, сопротивление R, добротность Q и коэффициент затухания damping_coefficient.
Вызов функции:
Вызываем plot_damped_oscillation со всеми вычисленными параметрами.
Как использовать:

Сохраните код в файл с расширением .py, например, damped_oscillation_plot.py.

Убедитесь, что у вас установлена библиотека matplotlib. Если нет, установите ее с помощью pip:

pip install matplotlib
Запустите программу из командной строки:

python damped_oscillation_plot.py
После запуска программы вы увидите окно с графиком затухающих колебаний.

Замечания:

Мы использовали стандартные функции Python (например, math.exp, math.cos, math.pi, math.sqrt) вместо numpy.
Количество точек и продолжительность графика можно регулировать параметрами num_points и duration.
Этот код поможет вам визуализировать затухающие колебания в колебательном контуре без использования numpy. Если у вас возникнут вопросы, не стесняйтесь спрашивать.

 
Файл не выбран
Message ChatGPT

Experience ChatGPT, fast and simple. Smart Chatbot with a huge knowledge base spanning all fields.











import matplotlib.pyplot as plt
import math

def calculate_damped_oscillation(time, amplitude, frequency, damping_coefficient):
    """
    Вычисляет напряжение в контуре с затухающими колебаниями.

    Args:
        time (float): Время (секунды).
        amplitude (float): Начальная амплитуда напряжения (вольты).
        frequency (float): Частота колебаний (Гц).
        damping_coefficient (float): Коэффициент затухания.

    Returns:
        float: Напряжение в контуре.
    """

    angular_frequency = 2 * math.pi * frequency
    voltage = amplitude * math.exp(-damping_coefficient * time) * math.cos(angular_frequency * time)
    return voltage

def calculate_envelope(time, amplitude, damping_coefficient):
   """
    Вычисляет огибающую затухания.

    Args:
        time (float): Время (секунды).
        amplitude (float): Начальная амплитуда напряжения (вольты).
        damping_coefficient (float): Коэффициент затухания.

    Returns:
        float: Огибающая напряжения.
    """
   return amplitude * math.exp(-damping_coefficient * time)

def plot_damped_oscillation_schematic(amplitude, frequency, damping_coefficient, duration=0.000002, num_points=500):
    """
    Строит схематичный график затухающих колебаний.

    Args:
        amplitude (float): Начальная амплитуда напряжения (вольты).
        frequency (float): Частота колебаний (Гц).
        damping_coefficient (float): Коэффициент затухания.
        duration (float): Длительность отображаемого времени (секунды).
        num_points (int): Количество точек для построения графика.
    """
    t_values = [duration * i / num_points for i in range(num_points)]
    u_values = [calculate_damped_oscillation(t, amplitude, frequency, damping_coefficient) for t in t_values]
    envelope_values = [calculate_envelope(t, amplitude, damping_coefficient) for t in t_values]
    negative_envelope_values = [-x for x in envelope_values]

    # Создание графика
    plt.figure(figsize=(10, 6))
    plt.plot(t_values, u_values, label='Затухающие колебания', color='blue', linewidth = 0.8)
    plt.plot(t_values, envelope_values, label = 'Огибающая затухания', color = 'red', linestyle = '--')
    plt.plot(t_values, negative_envelope_values,  color = 'red', linestyle = '--')


    plt.xlabel('Время (с)')
    plt.ylabel('Напряжение (В)')
    plt.title('Схематичный график затухающих колебаний')
    plt.grid(True)
    plt.legend()
    plt.show()

# Заданные параметры
C = 2e-9  # Ф
L = 0.15e-3  # Гн
Um = 0.9  # В
P = 1e-4  # Вт

# Расчет частоты
omega = 1 / math.sqrt(L * C)
frequency = omega / (2 * math.pi)

# Уменьшим частоту для более наглядного графика
frequency = frequency/10
# Расчет сопротивления
R = Um**2 / (2 * P)

# Расчет добротности
Q = (omega * L) / R

# Расчет коэффициента затухания
damping_coefficient = omega / (2 * Q)

plot_damped_oscillation_schematic(Um, frequency, damping_coefficient)
Изменения в коде:

plot_damped_oscillation_schematic: Функция была переименована для наглядности, а также теперь строит затухающие колебания и огибающую затухания.
Ограничение по времени: Время отображения (параметр duration) было уменьшено до 0.000002, чтобы показать только начальную часть затухания.
Упрощенный график: Добавлено построение огибающей затухания, используя calculate_envelope.
Меньшая частота: Частота колебаний была уменьшена в 10 раз для лучшего визуального восприятия схемы затухания.
Подписи: Добавлен заголовок к графику, уточнены подписи к осям и добавлена легенда.
Как использовать:

Сохраните код в файл с расширением .py, например, damped_oscillation_schematic.py.

Убедитесь, что у вас установлена библиотека matplotlib.

Запустите программу из командной строки:

python damped_oscillation_schematic.py
После запуска вы увидите схематичный график затухающих колебаний, где хорошо видна огибающая затухания, а колебания затухают за короткий промежуток времени.

Этот код должен сделать график более похожим на то, что мы рисовали схематично, выделяя основные характеристики затухающих колебаний.

 
Файл не выбран
Message ChatGPT

Experience ChatGPT, fast and simple. Smart Chatbot with a huge knowledge base spanning all fields.
