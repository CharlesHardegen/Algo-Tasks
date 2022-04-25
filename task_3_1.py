
from random import randint

def check_near(field, x, y):
    if field[x][y] == 0:
        if field[x-1][y-1] != 0:
            return False
        if field[x][y-1] != 0:
            return False
        if field[x+1][y-1] != 0:
            return False
        if field[x-1][y] != 0:
            return False
        if field[x+1][y] != 0:
            return False
        if field[x-1][y+1] != 0:
            return False
        if field[x][y+1] != 0:
            return False
        if field[x+1][y+1] != 0:
            return False
        return True
    else:
        return False

def set_ship(field, width, height):
    x, y = randint(1, width), randint(1, height)
    if check_near(field, x, y):
        field[x][y] = 1
    else:
        set_ship(field, width, height)


def print_field(field, width, height):
    
    width_str = '     '
    for i in range(width):
        width_str += '%4d '%(i+1)
    print(width_str)

    for i in range(height):
        print('%4d '%(i+1), end='')
        for j in range(width):
            print('%4s '%field[i][j], end="")
        print('')


def shot_cords(field, x, y):

    if field[x+1][y+1] == 0:
        return 'Empty'
    elif field[x+1][y+1] == 1:
        return 'Ship'
    elif field[x+1][y+1] == 2:
        return 'Already'


def game_process(n, m, l, field_1, field_2, user_field_1, user_field_2):
    turn = 0
    player_1_ships_defeated = 0
    player_2_ships_defeated = 0
    while True:
        if player_1_ships_defeated >= l:
            print('\n\n\tИгрок 2 победил!')
            break
        elif player_2_ships_defeated >= l:
            print('\n\n\tИгрок 1 победил')
            break

        if turn == 0:
            print('\n\tХОДИТ ПЕРВЫЙ ИГРОК\n')
            print_field(user_field_2, n, m)
            for i in range(l - player_1_ships_defeated):
                print('Введи координаты для стрельбы')
                x, y = map(int, input().split())
            
                result = shot_cords(field_2, x, y)
                if result == 'Empty':
                    user_field_2[x-1][y-1] = 'E'
                elif result == 'Ship':
                    user_field_2[x-1][y-1] = 'X'
                    player_2_ships_defeated += 1
                elif result == 'Already':
                    print('Ты уже стрелял по данным координатам. Ход уходит от тебя(')
                field_2[x][y] = 2

                print_field(user_field_2, n, m)
        elif turn == 1:
            print('\n\tХОДИТ ВТОРОЙ ИГРОК\n')
            print_field(user_field_1, n, m)
            for i in range(l - player_2_ships_defeated):
                print('Введи координаты для стрельбы')
                x, y = map(int, input().split())
            
                result = shot_cords(field_1, x, y)
                if result == 'Empty':
                    user_field_1[x-1][y-1] = 'E'
                elif result == 'Ship':
                    user_field_1[x-1][y-1] = 'X'
                    player_1_ships_defeated += 1
                elif result == 'Already':
                    print('Ты уже стрелял по данным координатам. Ход уходит от тебя(')
                field_1[x][y] = 2

                print_field(user_field_1, n, m)


        if turn == 1:
            turn = 0
        else:
            turn = 1


def run_game():
    # generate fields
    n, m, l = map(int, input().split())
    field_1 = [[0] * (n+2) for i in range(m+2)]
    for i in range(l+1):
        set_ship(field_1, n, m)

    field_2 = [[0] * (n+2) for i in range(m+2)]
    for i in range(l+1):
        set_ship(field_2, n, m)

    #user fields 
    user_field_1 = [['O'] * (n) for i in range(m)]
    user_field_2 = [['O'] * (n) for i in range(m)]

    #game process 
    game_process(n, m, l, field_1, field_2, user_field_1, user_field_2)



if __name__ == '__main__':
    run_game()
