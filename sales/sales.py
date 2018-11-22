""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
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
    table = data_manager.get_table_from_file("sales/sales_test.csv")
    options = (["Show table",
                "Add to table",
                "Remove from table",
                "Update the table",
                "Get the lowest price from the table",
                "Get items sold between dates"])
    while True:
        ui.print_menu("Sales menu", options, "Back to main menu")
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
            ui.print_result(get_lowest_price_item_id(table), "Lowest price item's ID")
        elif option == "6":
            dates = ui.get_inputs(["Month from", "Day from", "Year from", "Month to", "Day to", "Year to"],"Please give dates")
            show_table(get_items_sold_between(table, int(dates[0]), int(dates[1]), int(dates[2]), int(dates[3]), int(dates[4]), int(dates[5])))
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
    title_list = ["ID", "Title", "Price", "Month", "Day", "Year"]
    ui.print_table(table, title_list)

def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    title_list = ["Title", "Price", "Month", "Day", "Year"]
    inputs = [] 
    id_ = common.generate_random(table)
    inputs.extend(ui.get_inputs(title_list, "Please provide the required information"))
    inputs.insert(0,id_)
    table.append(inputs)
    data_manager.write_table_to_file("sales/sales_test.csv", table)
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

    inputs = []
    inputs.extend(ui.get_inputs(["ID"], "ID of removable item"))
    for lst in table:
        if inputs[0] in lst:
            table.remove(lst)
    data_manager.write_table_to_file("sales/sales_test.csv", table)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record


    id_index = 0
    inputs = []
    id_ = ui.get_inputs(["ID: "], "Choose an ID to update: ")
    for row in table:
        if row[0] == id_[0]:
            inputs.extend(ui.get_inputs(["Title: ", "Price: ", "Month: ", "Day: ", "Year: "], "Please provide the necessary information: "))
            for i in range(len(inputs)):
                table[id_index][i+1] = inputs[i-1]
        else:    
            id_index += 1
    data_manager.write_table_to_file("sales/sales_test.csv", table)
    start_module()
    return table"""
    
    id_index = 0
    wrong_id = True
    while wrong_id:
        id_ = ui.get_inputs(["ID: "], "Choose an ID to update: ")
        for row in table:
            if row[0] == id_[0]:
                table[id_index] = ui.get_inputs(["Title", "Price", "Month", "Day", "Year"], "Please provide the necessary information: ")
                table[id_index].insert(0, id_[0])
                wrong_id = False
            else:
                id_index += 1
    data_manager.write_table_to_file("sales/sales_test.csv", table)
    return table



# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code
    lowest_id = table[0][0]
    lowest_title = table[0][1]
    lowest_price = int(table[0][2])
    for line in table:
        id_ = line[0]
        title = line[1]
        price = int(line[2])
        if price < lowest_price:
            lowest_id = id_
            lowest_price = price
            lowest_title = title
        if price == lowest_price and title > lowest_title:
            lowest_title = title
            lowest_id = id_
    return lowest_id


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """
    result = []
    # from_date = date(year_from, month_from, day_from)
    # to_date = date(year_to, month_to, day_to)
    for row in table:
        sale_month = int(row[3])
        sale_day = int(row[4])
        sale_year = int(row[5])
        # sale_date = date(sale_year, sale_month, sale_day)
        if year_from <= sale_year <= year_to:
            if month_from <= sale_month <= month_to:
                if day_from <= sale_day <= day_to:
                    result.append(row)
    return result[1]
