salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_spend = 0 # общие расходы
for _ in range(months):
    total_spend += spend  # добавляем текущие расходы
    spend *= (1 + increase)  # здесь я решил увеличить расходы на 3% для следующего месяца
money_capital = total_spend - (salary * months)
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
