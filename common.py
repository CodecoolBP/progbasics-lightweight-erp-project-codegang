""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    nums = ['1','2','3','4','5','6','7','8','9','0']
    lowers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppers =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    specials = ['§','+', '!', '%', '/', '=', '(', ')', '~', 'ˇ', 'ˇ', '^', '˘', '°', '|', 'Ä', '€', 'Í', '÷', '×', 'ä', 'đ', 'Đ', 'í', 'ł', 'Ł', '$', 'ß', '¤', '<', '>', '#', '&', '@', '.']
    characters = [nums,lowers,uppers,specials]
    id_ = ''
    is_id_new = False

    while is_id_new == False:
        for character in characters:
            id_ += random.choice(character)
            id_ += random.choice(character)
        id_ = ''.join(random.sample(id_, len(id_)))
        if id_ not in table:
            is_id_new = True

    generated = id_

    # your code

    return generated

