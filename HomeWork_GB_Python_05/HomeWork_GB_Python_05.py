from random import randint

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
                    print(f"○", end=" ")
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
                    print(f"○", end=" ")
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

move_counter = 1
player_counter = 0
enemy_counter = 0
new_map_enemy = [[0] * 10 for i in range(10)]
new_map_palyer = [[0] * 10 for i in range(10)]
SetBattleMapOneBoat(new_map_enemy)
SetBattleMapOneBoat(new_map_palyer)
SetBattleMapTwoBoat(new_map_enemy)
SetBattleMapTwoBoat(new_map_palyer)

print(f"\n================= Поле противника =================\n")
PrintMap(new_map_enemy,False)
print(f"\n================= Ваше поле =================\n")
PrintMap(new_map_palyer,True)
print(f"\n================= Ход {move_counter} =================\n")