# entering distance
distance = float(input("Введіть відстань до дачі, км: "))
# entering of fuel consumption
consumption = float(input(
    "Введіть споживання палива Вашим авто на 100 км пробігу: "))
# entering fuel price
price = float(input("Введіть ціну 1 літру бензину: "))


def cost_travel(distance, consumption, price):
    # calculate the cost of trip
    result = round(distance*2*consumption/100*price, 2)
    print("** Вартість поїдки на дачу становитиме: ", result, " грн.")


cost_travel(distance, consumption, price)