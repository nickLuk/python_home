# Програма пошуку святкових днів
day = int(input("Введіть день місяця: "))
mount = int(input("Введіть місяць: "))


def holy(day, mount):
    if day == 1 and mount == 1:
        print("<<<Новий рік>>")
    elif day == 7 and mount == 1:
        print("<<<Різдво>>>")
    elif day == 8 and mount == 3:
        print("<<<Міжнародний жіночий день>>>")
    elif day == 9 and mount == 5:
        print("<<<День перемоги>>>")
    elif day == 28 and mount == 6:
        print("<<<День конституції>>>")
    elif day == 24 and mount == 8:
        print("<<<День незалежності>>>")
    else:
        print("Цього свята нема в базі")
    

    
holy(day, mount)