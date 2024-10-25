money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months = 0
current_capital = money_capital

while current_capital >= spend:
    current_capital += salary  # Добавляем зарплату к капиталу
    months += 1
    spend *= (1 + increase)  # Увеличиваем траты на процент роста цен
    current_capital -= spend  # Вычитаем траты из капитала

print("Количество месяцев, которое можно протянуть без долгов:", months)

