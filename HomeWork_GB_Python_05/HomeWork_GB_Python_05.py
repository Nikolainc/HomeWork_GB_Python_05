from random import randint, random

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
                if array[i][j] == 0 or array[i][j] == 5:
                    print(f"■", end=" ")
                elif array[i][j] == 7:
                    print(f"○", end=" ")
                elif array[i][j] == 9:
                    print(f"☑", end=" ")
                elif array[i][j] == 1:
                    print(f"□", end=" ")
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
                if array[i][j] == 0 or array[i][j] == 1 or array[i][j] == 5:
                    print(f"■", end=" ")
                elif array[i][j] == 7:
                    print(f"○", end=" ")
                elif array[i][j] == 9:
                    print(f"☑", end=" ")
            print("")

def IsPosition(array, Y, X):
    result = True
    for i in range(Y - 1, Y + 2):
        for j in range(X - 1, X + 2):
            if i < 0 or i > len(array) - 1 or j < 0 or j > len(array) - 1:
                continue
            if array[i][j] != 0:
                return False
    return result


def SetBattleMap(array, counter = 10):
    
    while counter > 0:
        Y = randint(0, len(array) - 1)
        X = randint(0, len(array) - 1)
        if IsPosition(array, Y, X):
            for i in range(Y - 1, Y + 2):
                for j in range(X - 1, X + 2):
                    if i < 0 or i > len(array) - 1 or j < 0 or j > len(array) - 1:
                        continue
                    array[i][j] = 5
            array[Y][X] = 1
            break
        counter -= 1


move_counter = 1
player_counter = 0
enemy_counter = 0
new_map_enemy = [[0] * 10 for i in range(10)]
new_map_palyer = [[0] * 10 for i in range(10)]
SetBattleMap(new_map_enemy)
SetBattleMap(new_map_palyer)

print(f"\n================= Поле противника =================\n")
PrintMap(new_map_enemy,False)
print(f"\n================= Ваше поле =================\n")
PrintMap(new_map_palyer,True)
print(f"\n================= Ход {move_counter} =================\n")