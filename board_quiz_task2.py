'''
https://github.com/Adeon18/skyscrapers
'''


def check_rows(board: list) -> bool:
    '''
    Check for row correction

    >>> check_rows(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''
    for row in board:
        used_elems = []
        for elem in row:
            if elem == ' ' or elem == '*':
                continue
            if int(elem) in range(1, 10) and int(elem) not in used_elems:
                used_elems.append(int(elem))
            elif int(elem) in range(1, 10) and int(elem) in used_elems:
                return False

    return True


def check_colls(board: list) -> bool:
    '''
    Check for col correction

    >>> check_colls(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    new_lst = []
    for i, row in enumerate(board):
        new_elem = ''
        for j, _ in enumerate(row):
            new_elem += board[j][i]
        new_lst.append(new_elem)

    return check_rows(new_lst)


def get_color_comb(board: list, horizontal_coord: int,\
                   vertical_coord: int) -> str:
    '''
    Get one color combiation data. Return the elements on one color
    '''
    line = ''
    for vertical in range(vertical_coord, vertical_coord+5):
        if board[vertical][horizontal_coord].isdigit():
            line += board[vertical][horizontal_coord]

    for horizontal in range(horizontal_coord, horizontal_coord+5):
        if board[vertical_coord+4][horizontal].isdigit():
            line += board[vertical_coord+4][horizontal]

    return line



def check_color(board: list) -> bool:
    '''
    Check for all colors, return False if any comb is wrong

    >>> check_color(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    True
    '''
    for i in range(0, 5):
        hor_coord = i
        vert_coord = 4-i
        combination = get_color_comb(board, hor_coord, vert_coord)
        if len(combination) != len(set(combination)):
            return False

    return True



def validate_board(board: list) -> bool:
    '''
    The main function for checking

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
"     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    '''
    if check_rows(board) and check_colls(board) and check_color(board):
        return True
    return False


if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
