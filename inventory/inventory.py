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
    while True:
        ui.print_menu("Inventory menu", options, "Back to main menu")
        inputs = ui.get_inputs(["Please enter a number"], "")
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
            title_list = ["ID", "Title", "Company", "Year", "Amount", "Availablity"]
            ui.print_table(get_available_items(table), title_list)
        elif option == "6":
            ui.print_result(get_average_durability_by_manufacturers(table), "Average durability by manufacturers")
        elif option == "0":
            break                       #ui.print_menu("Main menu", options, "Exit program")
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
    return table
    # your code


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
    inputs.extend(ui.get_inputs(title_list, "ID of removable item"))
    for lst in table:
        if inputs[0] in lst:
            table.remove(lst)
    data_manager.write_table_to_file("inventory/inventory_test.csv", table)
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
    id_index = 0
    inputs = []
    id_ = ui.get_inputs(["ID"], "Choose an ID to update: ")
    for row in table:
        if row[0] == id_[0]:
            inputs.extend(ui.get_inputs(["Title", "Company", "Year", "Amount"], "Please provide the necessary information"))
            for i in range(len(inputs)):
                table[id_index][i+1] = inputs[i-1]
        else:    
            id_index += 1
    data_manager.write_table_to_file("inventory/inventory_test.csv", table)
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
    result = []
    counter = 0
    for row in table:
        result.append(row)
        purchase_year = int(row[-2])
        durability = int(row[-1])
        if purchase_year+durability >= 2018:
            result[counter].append("Available")
        else:
            result[counter].append("Not available")
        counter +=1
    return result
    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """
    counter = {}
    result = {}
    for row in table:
        manufacturer = row[2]
        durability = int(row[-1])
        if manufacturer not in result:
            result[manufacturer] = durability
            counter[manufacturer] = 1
        else:
            result[manufacturer] += durability
            counter[manufacturer] += 1
    for key in counter:
        result[key] = result[key]/counter[key]
    return result
    # your code
