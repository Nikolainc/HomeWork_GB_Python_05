from itertools import count
from random import randint
from time import sleep
import time

# 0 - пустое поле, 1 - корабль, 7 - выстрел без попадания, 9 - попадание

def PrintMap(array, view = False):
    if view:
        print("Y:    ", end="")
        for i in range(len(array)):
            print(f"{i}", end=" ")
        print("")
        print("     ", end=" ")
        for i in range(len(array)):
            print("-", end=" ")
        print("")
        for i in range(len(array)):
            print(f"X: {i}| ", end="")
            for j in range(len(array[i])):
                if array[i][j] == 0:
                    print(f"■", end=" ")
                elif array[i][j] == 7:
                    print(f"X", end=" ")
                elif array[i][j] == 9:
                    print(f"☑", end=" ")
                elif array[i][j] == 1:
                    print(f"□", end=" ")
                else:
                    print(f"■", end=" ")
            print("")
    else:
        print("Y:    ", end="")
        for i in range(len(array)):
            print(f"{i}", end=" ")
        print("")
        print("     ", end=" ")
        for i in range(len(array)):
            print("-", end=" ")
        print("")
        for i in range(len(array)):
            print(f"X: {i}| ", end="")
            for j in range(len(array[i])):
                if array[i][j] == 0 or array[i][j] == 1:
                    print(f"■", end=" ")
                elif array[i][j] == 7:
                    print(f"X", end=" ")
                elif array[i][j] == 9:
                    print(f"☑", end=" ")
                else:
                    print(f"■", end=" ")
            print("")

def CountOfBoats(array):
    counter = 0
    for i in range(0,len(array)):
        for j in range(0, len(array)):
            if array[i][j] == 1:
                counter += 1
    return counter

def IsPosition(array, Y, X):
    result = True
    for i in range(Y - 1, Y + 2):
        for j in range(X - 1, X + 2):
            if i < 0 or i > len(array) - 1 or j < 0 or j > len(array) - 1:
                continue
            if array[i][j] != 0:
                return False
    return result

def GetRandomPosition(array):
    return randint(0,len(array)-1)

def SetBattleMapOneBoat(array):
    while CountOfBoats(array) < 5:
        Y = GetRandomPosition(array)
        X = GetRandomPosition(array)
        if IsPosition(array, Y, X):
            for i in range(Y - 1, Y + 2):
                for j in range(X - 1, X + 2):
                    if i < 0 or i > len(array) - 1 or j < 0 or j > len(array) - 1:
                        continue
                    array[i][j] = 5
            array[Y][X] = 1

def SetBattleMapTwoBoat(array):
    while CountOfBoats(array) < 9:
        Y_1 = GetRandomPosition(array)
        X_1 = GetRandomPosition(array)
        if randint(0,1) == 0:
            if Y_1 == 0:
                Y_2 = Y_1 + 1
            else:
                Y_2 = Y_1 - 1
            X_2 = X_1
        else:
            if X_1 == 0:
                X_2 = X_1 + 1
            else:
                X_2 = X_1 - 1
            Y_2 = Y_1
        if IsPosition(array, Y_1, X_1) and IsPosition(array, Y_2, X_2):
            for i in range(Y_1 - 2, Y_1 + 3):
                for j in range(X_1 - 2, X_1 + 3):
                    if i < 0 or i > len(array) - 1 or j < 0 or j > len(array) - 1:
                        continue
                    array[i][j] = 5
            for i in range(Y_2 - 2, Y_2 + 3):
                for j in range(X_2 - 2, X_2 + 3):
                    if i < 0 or i > len(array) - 1 or j < 0 or j > len(array) - 1:
                        continue
                    array[i][j] = 5
            array[Y_1][X_1] = 1
            array[Y_2][X_2] = 1

def MakeTurn(array, player = False):
    if player:
        while True:
            Y = int(input("Введите координаты по Y для нанесения удара: "))
            if Y < 0 or Y > len(array) - 1:
                continue
            X = int(input("Введите координаты по X для нанесения удара: "))
            if X < 0 or X > len(array) - 1:
                continue
            if array[Y][X] == 1:
                array[Y][X] = 9
                return True
            else:
                array[Y][X] = 7
                return False
    else:
        Y = randint(0, len(array) - 1)
        X = randint(0, len(array) - 1)
        if array[Y][X] == 1:
            array[Y][X] = 9
            return True
        else:
            array[Y][X] = 7
            return False

move_counter = 1
map_enemy = [[0] * 10 for i in range(10)]
map_palyer = [[0] * 10 for i in range(10)]
SetBattleMapOneBoat(map_enemy)
SetBattleMapOneBoat(map_palyer)
SetBattleMapTwoBoat(map_enemy)
SetBattleMapTwoBoat(map_palyer)

print(f"\n================= Поле противника =================\n")
PrintMap(map_enemy, False)
print(f"\n================= Ваше поле =================\n")
PrintMap(map_palyer, True)

while CountOfBoats(map_palyer) > 0 or CountOfBoats(map_enemy) > 0:
    print(f"\n================= Ваш ход {move_counter} =================\n")
    print(f"У противника {CountOfBoats(map_enemy)} кораблей")
    if MakeTurn(map_enemy, True):
        print("\n||||| Попадание! |||||")
    else:
        print("\n||||| Промах! |||||")
    move_counter += 1
    print(f"\n================= Поле противника =================\n")
    PrintMap(map_enemy, False)
    time.sleep(randint(1, 3))
    if MakeTurn(map_palyer, False):
        print("\n||||| Попадание! |||||")
    else:
        print("\n||||| Промах! |||||")
    print(f"\n================= Ваше поле =================\n")
    PrintMap(map_palyer, True)

if CountOfBoats(map_palyer) > 0:
    print("Победа!")
else:
    print("Мы проиграли эту битву..")