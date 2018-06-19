from random import randint
import copy

FIELD_SIZE = 10
MINES_QUANTITY = 10
EMPTY_CELL = '*'
MINE = 'M'

end = ' '
def get_playing_field():
    """
    returns field for minesweeper game
    """
    return [
        [EMPTY_CELL for i in range(FIELD_SIZE)]
        for i in range(FIELD_SIZE)
        ]


# {
def get_random_coord(field_size):
    return randint(0, field_size - 1)


def set_mines(field):
    """
    returns random mined field for game
    """
    mines = 0
    while mines < MINES_QUANTITY:
        x, y = get_random_coord(FIELD_SIZE), get_random_coord(FIELD_SIZE)
        if field[x][y] != EMPTY_CELL:
            continue
        field[x][y] = MINE
        mines += 1
    return field


# }


# {
def is_coords_in_range(x, y):
    return 0 <= x < FIELD_SIZE and 0 <= y < FIELD_SIZE


def is_mine(x, y, field):
    return field[x][y] == MINE


def flag_calculator(flags):
    print('Left', (MINES_QUANTITY - len(flags)), 'mines')


def mine_calculation(field, x, y):
    """
    returns the quantity of mines in neighboring cells
    """
    if field[x][y] == MINE:
        return 'M'

    mines = 0
    for range_x in (-1, 0, 1):
        for range_y in (-1, 0, 1):
            x_offset, y_offset = x + range_x, y + range_y
            if is_coords_in_range(x_offset, y_offset) and \
                    is_mine(x_offset, y_offset, field):
                mines += 1
    return mines


def print_open_field(field, playground_mines):
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(mine_calculation(field, i, j), end)
            playground_mines[i][j] = (mine_calculation(field, i, j))
        print()


def open_field(field, playground_mines):
    for i in range(len(field)):
        for j in range(len(field[i])):
            playground_mines[i][j] = (mine_calculation(field, i, j))


# }


def input_coordinates(playing_field, playground_mines):
    """
    Inputs of cell coordinates
    """
    while True:
        try:
            x = input('Write number of line from 0 to %s:' % (FIELD_SIZE - 1))
            if x == 'test':
                test_game(playing_field, playground_mines)
            y = input('Write number of line from 0 to %s:' % (FIELD_SIZE - 1))
            if y == 'test':
                test_game(playing_field, playground_mines)
            elif not is_coords_in_range(int(x), int(y)):
                raise TypeError
            return int(x), int(y)
        except ValueError:
            print('Wrong input, try again')
        except TypeError:
            print('Your number of coordinate is out of field')


def validated(x, y, playing_field):
    """
    Check for repeated call to the cell
    """
    # user_input_cell = (x, y)
    if playing_field[x][y] == '*':
        True
    else:
        return False


def action():
    """
    Choose an action to open the cell or mark as Flag
    """
    while True:
        act = input('Enter O - to open cell / F - to mark as FLAG').upper()
        if act == 'O':
            return 'O'
        elif act == 'F':
            return 'F'
        elif act == 'test':
            return 'test'
        else:
            continue


def mark_mine(x, y, flag, playing_field, flags):
    """
    set the flag
    """
    if flag == 'F':
        playing_field[x][y] = 'F'
        flags.append(1)
        # flag_calculator(flags)


def open_cell(x, y, action, playing_field, playground_mines):
    if action == 'O':
        playing_field[x][y] = playground_mines[x][y]
        if playing_field[x][y] == 'M':
            print('Game Over')
            test_game(playing_field, playground_mines)
        else:
            return True
    elif action == 'test':
        test_game(playing_field, playground_mines)


def print_field(field):
    print(' ', ' ', end)
    for i in range(len(field)):
        print(i, end)
        print()
        print(' ', ' ', end)
        for i in range(len(field)):
            print('–', end)
            print()
            for i in range(len(field)):
                print(i, '|', end)
                for j in range(len(field[i])):
                    print(field[i][j], end)
                    # show_playground_mines[i][j] = (mine_calculation(field, i, j))
                    print()

            def create_mini_range(playground_mines, x, y):
                rows = range(max(0, x - 1), min(len(playground_mines[0]), x + 2))
                cols = range(max(0, y - 1), min(len(playground_mines), y + 2))
                return rows, cols
                # open_zero(playground_mines, rows, cols, playing_field)

            def open_zero(playground_mines, rows, cols, playing_field):
                '''
                Если открытое поле Ноль -- открывает вокруг ячейки
                '''
                zero_list = [playing_field[row][col] for row in rows for col in cols]
                zeros = []
                for row in rows:
                    for col in cols:
                        playing_field[row][col] = playground_mines[row][col]
                        if playing_field[row][col] == 0:
                            zeros.append((row, col))
                return zeros, zero_list

            def cell_zero(playing_field, x, y, playground_mines, *args):
                if playground_mines[x][y] == 0:
                    rows, cols = create_mini_range(playground_mines, x, y)
                    zeros, zero_list = open_zero(playground_mines, rows, cols, playing_field)
                    for z in zeros:
                        x, y = z
                        if playing_field[x][y] == 0 and '*' in zero_list:
                            cell_zero(playing_field, x, y, playground_mines)

            def clear_cell(playing_field, x, y, flags):
                playing_field[x][y] = '*'
                flags.pop(0)

            def redefine_coordinates(cell):
                if cell == 'F':
                    print('Are you want to clean the cell?')
                    while True:
                        clear = input('y/n ').lower()
                        if clear == 'n':
                            return False
                        elif clear == 'y':
                            return True
                        else:
                            continue

            def test_game(playing_field, playground_mines):
                test_list = []
                for row in range(len(playing_field)):
                    for cell in range(len(playing_field[row])):
                        if playing_field[row][cell] == 'F':
                            if playground_mines[row][cell] != 'M':
                                test_list.append((row, cell))
                        if playground_mines[row][cell] == 'M':
                            if playing_field[row][cell] != 'F':
                                test_list.append((row, cell))
                print(test_list)
                exit_game(test_list, playground_mines)

            def exit_game(test_list, playground_mines):
                if len(test_list) > 0:
                    print('You lose!')
                    for t in test_list:
                        print('Error in the cell', t)
                else:
                    print('Congratulations, you win!!!')
                exit()

            def start_game(flags, playing_field, playground_mines):
                while True:
                    flag_calculator(flags)
                    x, y = input_coordinates(playing_field, playground_mines)
                    if validated(x, y, playing_field) == False:
                        print('Enter the used coordinates')
                        clear = redefine_coordinates(playing_field[x][y])
                        if clear == True:
                            clear_cell(playing_field, x, y, flags)
                            print_field(playing_field)
                            continue
                        else:
                            continue
                    cell_zero(playing_field, x, y, playground_mines)
                    do_action = action()  # Открываем ячеку или присваеваем ей Флаг
                    mark_mine(x, y, do_action, playing_field, flags)
                    opened_cell = open_cell(x, y, do_action, playing_field, playground_mines)
                    print_field(playing_field)

            def create_game():
                playing_field = get_playing_field()  # Создаем игровое поле
                mines_field = get_playing_field()  # Создаем поле для хранения мин
                mines_field = set_mines(mines_field)  # Расставляем мины
                playground_mines = get_playing_field()  # Создаем поле, видемое игроку
                open_field(mines_field, playground_mines)  # Создаем открытое поле
                # inputs_cell = []   # Enter the list to store the "def input_coordinates():"
                # print_open_field(mines_field, playground_mines)
                print_field(playing_field)  # Печатаем поле
                flags = []
                start_game(flags, playing_field, playground_mines)

            def main():
                create_game()

            if __name__ == '__main__':
                main()