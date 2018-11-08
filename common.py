""" Common module
implement commonly used functions here
"""

import random
import ui
import data_manager
import hr

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

def sort_abc(str1, str2):
    if str2.startswith(str1) and len(str1) < len(str2):
        return True
    elif str1.startswith(str2) and len(str2) < len(str1):
        return False
    if str1[0] == str2[0]:
        return sort_abc(str1[1:], str2[1:])
    else:
        return str1[0] < str2[0]