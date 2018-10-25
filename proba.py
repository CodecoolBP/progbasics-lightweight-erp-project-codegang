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

print_menu("Main", title_list , "lépjki pls")