""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
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
    table = data_manager.get_table_from_file("inventory/inventory_test.csv")
    options = (["Show table",
                "Add to table",
                "Remove from table",
                "Update item",
                "Available items",
                "Average durability by manufacturers"])
    ui.print_menu("Inventory menu", options, "Back to main menu")
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
        pass
    elif option == "6":
        pass
    elif option == "0":
        pass                       #ui.print_menu("Main menu", options, "Exit program")
    else:
        raise KeyError("There is no such option.")
    # your code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["ID", "Title", "Company", "Year", "Amount"]
    ui.print_table(table, title_list)
    start_module()
    # your code


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """
    title_list = ["Title", "Company", "Year", "Amount"]
    inputs = [] 
    id_ = common.generate_random(table)
    inputs.extend(ui.get_inputs(title_list, "Please provide the required information"))
    inputs.insert(0,id_)
    table.append(inputs)
    data_manager.write_table_to_file("inventory/inventory_test.csv", table)
    start_module()
    return table
    # your code

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
    value = False
    id_ = input("ID of the record: ")
    for lst in table:
        if id_ in lst:
            table.remove(lst)
            value = True
    if value == False:
        print('not in table')
    data_manager.write_table_to_file("inventory/inventory_test.csv", table)
    start_module()
    return table
    # your code

    return table


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
            table[counter-1][1] = input("Title: ")
            table[counter-1][2] = input("Company: ")
            table[counter-1][3] = input("Year: ")
            table[counter-1][4] = input("Amount: ")
    data_manager.write_table_to_file("inventory/inventory_test.csv", table)
    start_module()
    return table
    # your code

    return table


# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
