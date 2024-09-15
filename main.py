import numpy as np
import matplotlib.pyplot as plt

# Константы
g = 9.81  # Ускорение свободного падения, м/с^2


# Функция для расчета траектории движения
def calculate_trajectory(h, v0, theta):
    # Перевод угла в радианы
    theta_rad = np.radians(theta)

    # Время подъема до максимальной точки
    t_max = v0 * np.sin(theta_rad) / g

    # Время падения с максимальной высоты
    h_max = h + (v0 * np.sin(theta_rad)) ** 2 / (2 * g)
    t_fall = np.sqrt(2 * h_max / g)

    # Общее время полета
    T = 2 * t_max + t_fall

    # Время для построения траектории
    t = np.linspace(0, T, num=500)

    # Расчет координат
    x = v0 * np.cos(theta_rad) * t
    y = h + v0 * np.sin(theta_rad) * t - 0.5 * g * t ** 2

    # Фильтр для положительных значений y
    valid_indices = y >= 0
    t = t[valid_indices]
    x = x[valid_indices]
    y = y[valid_indices]

    return t, x, y


# Функция для расчета скорости в каждый момент времени
def calculate_velocity(v0, theta, t):
    theta_rad = np.radians(theta)
    vx = v0 * np.cos(theta_rad)
    vy = v0 * np.sin(theta_rad) - g * t
    v = np.sqrt(vx ** 2 + vy ** 2)
    return v


# Визуализация движения
def visualize(h, v0, theta):
    # Расчет траектории
    t, x, y = calculate_trajectory(h, v0, theta)

    # Расчет скорости
    v = calculate_velocity(v0, theta, t)

    # Построение графиков
    fig, axs = plt.subplots(3, 1, figsize=(8, 12))

    # График траектории
    axs[0].plot(x, y)
    axs[0].set_title('Траектория движения тела')
    axs[0].set_xlabel('Горизонтальная координата, м')
    axs[0].set_ylabel('Вертикальная координата, м')

    # График зависимости координат от времени
    axs[1].plot(t, x, label='x(t)')
    axs[1].plot(t, y, label='y(t)')
    axs[1].set_title('Координаты от времени')
    axs[1].set_xlabel('Время, с')
    axs[1].set_ylabel('Координаты, м')
    axs[1].legend()

    # График зависимости скорости от времени
    axs[2].plot(t, v)
    axs[2].set_title('Скорость от времени')
    axs[2].set_xlabel('Время, с')
    axs[2].set_ylabel('Скорость, м/с')

    # Отображение графиков
    plt.tight_layout()
    plt.show()


# Основная программа
if __name__ == '__main__':
    # Ввод данных
    h = float(input("Введите высоту (м): "))
    v0 = float(input("Введите начальную скорость (м/с): "))
    theta = float(input("Введите угол броска (градусы): "))

    # Визуализация траектории и графиков
    visualize(h, v0, theta)
