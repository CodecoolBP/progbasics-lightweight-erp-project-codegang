""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    table = data_manager.get_table_from_file("store/games_test.csv")
    options = (["Show table",
                "Add to table",
                "Remove from table",
                "Update the table",
                "Counts games by manufacturer",
                "Get items sold between dates"])
    while True:
        ui.print_menu("Store menu", options, "Back to main menu")
        inputs = ui.get_inputs(["Please enter a number: "], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            remove(table, id)
        elif option == "4":
            update(table, id)
        elif option == "5":
            get_counts_by_manufacturers(table)
        elif option == "6":
            pass
        elif option == "0":
            break                       #ui.print_menu("Main menu", options, "Exit program")
        else:
            raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    title_list = ["ID", "Title", "Manufacturer", "Price", "Stock"]
    table = data_manager.get_table_from_file("store/games_test.csv")
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    title_list = ["Title: ", "Manufacturer: ", "Price: ", "Stock: "]
    inputs = [] 
    id_ = common.generate_random(table)
    inputs.extend(ui.get_inputs(title_list, "Please provide the required information"))
    inputs.insert(0,id_)
    table.append(inputs)
    data_manager.write_table_to_file("store/games_test.csv", table)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    title_list = ["ID: "]
    inputs = []
    inputs.extend(ui.get_inputs(title_list, "ID of removable item:"))
    for lst in table:
        if inputs[0] in lst:
            table.remove(lst)
    data_manager.write_table_to_file("store/games_test.csv", table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record

    id_index = 0           #Reka's old function, in case of bug
    inputs = []
    id_ = ui.get_inputs(["ID: "], "Choose an ID to update: ")
    for row in table:
        if row[0] == id_[0]:
            inputs.extend(ui.get_inputs(["Title: ", "Manufacturer: ", "Price: ", "Stock: "], "Please provide the necessary information: "))
            for i in range(len(inputs)):
                table[id_index][i+1] = inputs[i-1]
        else:    
            id_index += 1
    data_manager.write_table_to_file("store/games_test.csv", table)
    start_module()
    return table"""

    id_index = 0
    wrong_id = True
    while wrong_id:
        id_ = ui.get_inputs(["ID: "], "Choose an ID to update: ")
        for row in table:
            if row[0] == id_[0]:
                table[id_index] = ui.get_inputs(["Title: ", "Manufacturer: ", "Price: ", "Stock: "], "Please provide the necessary information: ")
                table[id_index].insert(0, id_[0])
                wrong_id = False
            else:
                id_index += 1
    data_manager.write_table_to_file("store/games_test.csv", table)
    return table




# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (print(result)rk on

    Returns:
         dict: print(result)structure: { [manufacturer] : [count] }
    """

    # your code
    
    result = {}
    for i in table:
        if i[2] not in result:
            result[i[2]] = 0
    for i in table:
        if i[2] in result.keys():
            result[i[2]] += 1
    ui.print_result(result, 'Different kind of games in store of each manufacturer')

            



def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
