money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
total = 0  # количество месяцев без долгов
while money_capital + salary >= spend:
    money_capital += salary - spend
    spend += spend * increase
    total += 1
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
print("Количество месяцев, которое можно протянуть без долгов:", total)
