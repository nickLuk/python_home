# Обчислення швидкості спорсмена
distance = float(input("Введіть відстань, яку км пробіг спортсмен, м: "))
time = float(input("Введіть час, якийзатратив спортсмен,с: "))


def cost_travel(distance, time):
    speed = round(distance/time, 2)
    print("Швидкість спортсмена - ", speed, "м/с")

cost_travel(distance, time)