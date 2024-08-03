import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


### Обчислення інтеграла методом Монте-Карло ###


# Висота прямокутника
max_y = f(b)

# Кількість випадкових точок
num_points = 1000000

# Генерування випадкових точок
x_random = np.random.uniform(a, b, num_points)
y_random = np.random.uniform(0, max_y, num_points)

# Підрахунок точок під кривою
points_under_curve = sum(y_random < f(x_random))

# Оцінка площі
area = (b - a) * max_y * (points_under_curve / num_points)

print(f"Оцінка інтеграла методом Монте-Карло: {area}")


### Чисельне інтегрування ###

integral, error = quad(f, a, b)

print(f"Чисельне інтегрування: {integral}")
print(f"Похибка чисельного інтегрування: {error}")