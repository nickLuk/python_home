from random import randint

exit:True
user = 0
comp = 0
end_game = int(input("Enter number of points before the end of the gamee "))
while exit:
    input("Your turn ====>>")
    user_dice1 = randint(1, 6)
    user_dice2 = randint(1, 6)
    print("Dice one:", user_dice1, "Dice two:", user_dice2)
    input("PC turn ====>>")
    comp_dice1 = randint(1, 6)
    comp_dice2 = randint(1, 6)
    print("Dice one:", comp_dice1, "Dice two:", comp_dice2)
    if user_dice1 + user_dice2 > comp_dice1 + comp_dice2:
        user += 1
        if user_dice1 == user_dice2:
            user += 2
    elif user_dice1 + user_dice2 < comp_dice1 + comp_dice2:
        comp += 1
        if comp_dice1 == comp_dice2:
            comp += 2
    print("Total score:")
    print("Your score= ", user, "PC score= ", comp)
    if user ==  end_game or comp == end_game:
        break
if user > comp:
    print("!!!!!!! Win user !!!!!!")
else:
    print("!!!!!!! Win PC !!!!!!!!")
    
