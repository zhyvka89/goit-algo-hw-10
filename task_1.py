from pulp import *

# Створення нової задачі лінійного програмування
prob = LpProblem("Maximize_Production", LpMaximize)

# Визначення змінних
x1 = LpVariable("Lemonade", 0)  # Кількість "Лимонаду"
x2 = LpVariable("Fruit_Juice", 0)  # Кількість "Фруктового соку"

# Цільова функція: максимізувати загальну кількість продуктів
prob += x1 + x2, "Total_Production"

# Обмеження на ресурси
prob += 2*x1 + x2 <= 100, "Water_Constraint"
prob += x1 <= 50, "Sugar_Constraint"
prob += x1 <= 30, "Lemon_Juice_Constraint"
prob += 2*x2 <= 40, "Fruit_Puree_Constraint"

# Розв'язання задачі
prob.solve()

# Виведення результатів
print("Status:", LpStatus[prob.status])
print("Optimal quantity of Lemonade:", value(x1))
print("Optimal quantity of Fruit Juice:", value(x2))
print("Maximum total production:", value(prob.objective))