""" User Interface (UI) module """


def print_table(table, title_list):
    """
    Prints table with data.

    Example:
        /-----------------------------------\
        |   id   |      title     |  type   |
        |--------|----------------|---------|
        |   0    | Counter strike |    fps  |
        |--------|----------------|---------|
        |   1    |       fo       |    fps  |
        \-----------------------------------/

    Args:
        table (list): list of lists - table to display
        title_list (list): list containing table headers

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    try:
        longest_data_list = []
        for row in range(len(table[0])):
            longest_data_list.append(len(title_list[row]))
            for column in range(len(title_list)):
                if longest_data_list[row] < len(table[column][row]):
                    longest_data_list[row] = len(table[column][row])

        for i in range(len(longest_data_list)):
            longest_data_list[i] += 1

        line_lenght = 0

        for k in longest_data_list:
            line_lenght += k
        line_lenght += len(longest_data_list) * 3 + 3

        for k in range(line_lenght):
            print('-', end='')
        print('')

        print("|", end='')
        for i in range(len(title_list)):
            print("| {:^{space_length}} ".format(title_list[i], space_length=longest_data_list[i]), end='')
        print('||')
        for k in range(line_lenght):
            print('-', end='')
        print('')

        for i in range(len(table)):
            print("|", end='')
            for j in range(len(table[i])):
                print("| {:^{space_length}} ".format(table[i][j], space_length=longest_data_list[j]), end='')
            print("||")
            for k in range(line_lenght):
                print('-', end='')
            print('')
    except:
        print("Empty table")


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


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    counter = 1
    print(title + ": ")
    for option in list_options:
        print("\t(" + str(counter) + ") " + option)
        counter += 1
    print("\t(0) " + exit_message)


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []
    print(title)
    for data in list_labels:
        inputs.append(input(data + ": "))
    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print("Error: " + message)
