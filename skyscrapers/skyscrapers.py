"""
https://github.com/Adeon18/skyscrapers
"""


def read_input(path: str) -> list:
    """
    Read game board file from path.
    Return list of str.
    """
    with open(path, "r") as file:
        output_lst = file.read().split("\n")
        output_lst = output_lst[:-1]

    return output_lst


def left_to_right_check(input_line: str, pivot: int) -> bool:
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most
    hint is visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    >>> left_to_right_check("512345*", 5)
    True
    >>> left_to_right_check("4124531", 4)
    True
    """
    row = input_line
    max_num = 0
    count = 0
    for _, num in enumerate(row[1:-1]):
        # If the row is *, we move on to the next
        if num == "*":
            continue
        # Check if the current building is the one we need
        if int(num) > max_num:
            max_num = int(num)
            count += 1

    if count == pivot:
        return True
    return False


def check_not_finished_board(board: list) -> bool:
    """
    Check if skyscraper board is not finished, i.e.,
    '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*',\
'4?????*', '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*',\
'423145*', '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*',\
'423145*', '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for row in board:
        if "?" in row:
            return False
    return True


def check_uniqueness_in_rows(board: list) -> bool:
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length,
    False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
'*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    # We chop each row
    for row in board[1:-1]:
        elements_int = []
        for elem in row[1:-1]:
            # If element can't be converted to int, it is skipped
            try:
                if int(elem) in elements_int:
                    return False
                else:
                    elements_int.append(int(elem))
            except:
                continue
    return True


def check_horizontal_visibility(board: list) -> bool:
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    # Our right hint(default=*)
    right_req = "*"
    for row in board[1:-1]:
        # We keep track of the max element and seen buildings
        right_flag = 0
        max_elem_right = 0
        # We skip if there's no hint
        if row[0] == "*":
            continue
        else:
            right_req = int(row[0])
            for elem in row[1:-1]:
                # Check if the following element is bigger
                if int(elem) > max_elem_right:
                    max_elem_right = int(elem)
                    right_flag += 1
        # If the hints aren't met, we return False
        if right_flag != right_req:
            return False
    # Same code, another direction, rewritten for better readability
    left_req = "*"
    for row in board[1:-1]:
        left_flag = 0
        max_elem_left = 0
        if row[-1] == "*":
            continue
        else:
            left_req = int(row[-1])
            for elem in row[1:-1][::-1]:
                if int(elem) > max_elem_left:
                    max_elem_left = int(elem)
                    left_flag += 1
                    # print('left ', right_flag, right_req)

        if left_flag != left_req:
            return False

    return True


def check_columns(board: list) -> bool:
    """
    Check column-wise compliance of the board for
    uniqueness (buildings of unique height)
    and visibility (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in one
    function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*',\
'*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*',\
'*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    new_lst = []
    # Flip and check horisontally
    for i, row in enumerate(board):
        new_elem = ""
        for j, _ in enumerate(row):
            new_elem += board[j][i]
        new_lst.append(new_elem)

    if check_uniqueness_in_rows(new_lst) and check_not_finished_board(new_lst):
        return check_horizontal_visibility(new_lst)
    return False


def check_skyscrapers(input_path: str) -> bool:
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    board = read_input(input_path)
    # If everything is met return True
    if (
        check_horizontal_visibility(board)
        and check_columns(board)
        and check_uniqueness_in_rows(board)
        and check_not_finished_board(board)
    ):
        return True
    return False


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
