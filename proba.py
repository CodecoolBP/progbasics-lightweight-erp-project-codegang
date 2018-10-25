import random
title_list = ["egy","kettő","három"]
table = ([["one","dos","fgt"],
          ["drei","vier44","anyu"],
          ["cinco","seis","sdifhhsjd"]])

longest_data_list = []
for row in range(len(table[0])):
    longest_data_list.append(len(table[0][row]))
    for column in range(len(title_list)):
        if longest_data_list[row] < len(table[column][row]):
            longest_data_list[row] = len(table[column][row])

print(longest_data_list)

for i in range(len(longest_data_list)):
    longest_data_list[i] += 2
    

line_lenght = 0

for k in longest_data_list:
    line_lenght += k
line_lenght += len(table) * 3 + 3

for k in range(line_lenght):
    print('-', end = '')
print('')  

print("|", end = '')
for i in range(len(title_list)):
    print("| {:^{space_length}} ".format(title_list[i], space_length=longest_data_list[i]), end = '')
print('||')
for k in range(line_lenght):
    print('-', end = '')
print('')  

for i in range(len(table)):
    print("|", end = '')
    for j in range(len(table[i])):
        print("| {:^{space_length}} ".format(table[i][j], space_length=longest_data_list[j]), end = '')
    print("||")
    for k in range(line_lenght):
        print('-', end = '')
    print('')    


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print(label + ": " + str(result))
    # your code


def print_menu(title, list_options, exit_message):
    counter = 1
    print(title + ": ")
    for option in list_options:
        print("\t(" + str(counter) + ") " + option)
        counter += 1 
    print("\t(0) " + exit_message)
    select = input("Please, select an option.")
    if select == "0":
        return None



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
    

print(id_)


def remove(table, id_):
    for lst in table:
        if id_ in lst:
            table.remove(lst)

remove(table, "one")
print(table)

def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """
    counter = 0
    id_ = input("ID of the record: ")
    for lst in table:
        counter += 1
        if id_ in lst:
            table[counter][1] = input("Title: ")
            table[counter][2] = input("Price: ")
            table[counter][3] = input("Month: ")
            table[counter][4] = input("Day: ")
            table[counter][5] = input("Year: ")
    

update(table,id_)