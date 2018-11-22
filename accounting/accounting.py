""" Accounting module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD
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

    # your code
    table = data_manager.get_table_from_file("accounting/items_test.csv")
    options = (["Show table",
                "Add to table",
                "Remove from table",
                "Update the table",
                "Year of the highest profit",
                "Average profit per item in given year"])
    while True:
        ui.print_menu("Accounting menu", options, "Back to main menu")
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
            ui.print_result(which_year_max(table),"Best year")
        elif option == "6":
            input_data = ui.get_inputs(["Year"], "Enter a year")
            avg_amount(table, input_data[0])
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

    # your code
    title_list = ["ID", "Month", "Day", "Year", "Type", "Amount"]
    table = data_manager.get_table_from_file("accounting/items_test.csv")
    ui.print_table(table, title_list)

"""Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * month (number): Month of the transaction
    * day (number): Day of the transaction
    * year (number): Year of the transaction
    * type (string): in = income, out = outflow
    * amount (int): amount of transaction in USD"""

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code
    title_list = ["Month", "Day", "Year", "Type", "Amount"]
    inputs = [] 
    id_ = common.generate_random(table)
    inputs.extend(ui.get_inputs(title_list, "Please provide the required information"))
    inputs.insert(0,id_)
    table.append(inputs)
    data_manager.write_table_to_file("accounting/items_test.csv", table)
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

    # your code
    wrong_id = True
    while wrong_id:
        id_ = ui.get_inputs(["ID"], "Choose an ID to remove")
        for row in table:
            if row[0] == id_[0]:
                table.remove(row)
                wrong_id = False
    data_manager.write_table_to_file("accounting/items_test.csv", table)
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

    # your code
    
    id_index = 0
    wrong_id = True
    while wrong_id:
        id_ = ui.get_inputs(["ID"], "Choose an ID to update")
        for row in table:
            if row[0] == id_[0]:
                table[id_index] = ui.get_inputs(["Month", "Day", "Year", "Type", "Amount"], "Please provide the necessary information")
                table[id_index].insert(0, id_[0])
                wrong_id = False
            else:
                id_index += 1
    data_manager.write_table_to_file("accounting/items_test.csv", table)

#     * month (number): Month of the transaction
#     * day (number): Day of the transaction
#     * year (number): Year of the transaction
#     * type (string): in = income, out = outflow
#     * amount (int): amount of transaction in USD

    return table


# special functions:
# ------------------

def which_year_max(table):
    """
    Question: Which year has the highest profit? (profit = in - out)

    Args:
        table (list): data table to work on

    Returns:
        number
    """

    # your code
    best_year = ""
    highest_profit = 0
    yearly_profit = {}
    for line in table:
        year = line[3]
        in_or_out = line[4]
        amount = int(line[5])
        if year not in yearly_profit:
            if in_or_out == "in":
                yearly_profit[year] = amount
            else:
                yearly_profit[year] = 0-amount
        else:
            if in_or_out == "in":
                yearly_profit[year] += amount
            else:
                yearly_profit[year] -= amount
    for year in yearly_profit:
        if yearly_profit[year] > highest_profit:
            highest_profit = yearly_profit[year]
            best_year = year
    return best_year


def avg_amount(table, year):
    """
    Question: What is the average (per item) profit in a given year? [(profit)/(items count)]

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        number
    """

    profit = 0
    items_count = 0
    for row in table:
        if int(row[3]) == int(year):
            items_count += 1
            if row[4] == "in":
                profit += int(row[5])
            else:
                profit -= int(row[5])
    if items_count == 0:
        return items_count
    ui.print_result(profit / items_count, "Average profit in given year is")
    return profit / items_count
