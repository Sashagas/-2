salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
total_spend = 0
for i in range(1, months + 1):
    total_spend += spend * (1 + increase)**(i - 1)  # Суммируем траты за каждый месяц с учетом роста цен

safety_cushion = total_spend - (salary * months)  # Вычисляем подушку безопасности

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {round(safety_cushion)}")
