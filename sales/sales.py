""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
    * customer_id (string): id from the crm
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
            ui.print_result(get_items_sold_between(table, int(dates[0]), int(dates[1]), int(dates[2]), int(dates[3]), int(dates[4]), int(dates[5])),"Items sold betwrrn dates")
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
    """

    # your code

    # id_index = 0
    # inputs = []
    # id_ = ui.get_inputs(["ID: "], "Choose an ID to update: ")
    # for row in table:
    #     if row[0] == id_[0]:
    #         inputs.extend(ui.get_inputs(["Title: ", "Price: ", "Month: ", "Day: ", "Year: "], "Please provide the necessary information: "))
    #         for i in range(len(inputs)):
    #             table[id_index][i+1] = inputs[i-1]
    #     else:    
    #         id_index += 1
    # data_manager.write_table_to_file("sales/sales_test.csv", table)
    # start_module()
    # return table
    
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
    for row in table:
        sale_month = int(row[3])
        sale_day = int(row[4])
        sale_year = int(row[5])

        if year_from < sale_year < year_to:
            result.append(row)

        elif year_from == sale_year < year_to:
            if month_from < sale_month:
                result.append(row)
            elif sale_month == month_from:
                if day_from < sale_day:
                    result.append(row)

        elif year_from == sale_year and sale_year == year_to:
            if month_from == sale_month < month_to:
                if day_from < sale_day:
                    result.append(row)
            elif month_from == sale_month == month_to:
                if day_from < sale_day < day_to:
                    result.append(row)
            elif  month_from < sale_month == month_to:
                if sale_day < day_to:
                    result.append(row)
            elif month_from < sale_month < month_to:
                result.append(row)

        elif year_from < sale_year == year_to:
            if sale_month < month_to:
                result.append(row)
            elif sale_month == month_to:
                if sale_day < day_to:
                    result.append(row)

    return result
        
def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code


def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """

    # your code
# functions supports data abalyser
# --------------------------------
def get_title_by_id(id):
     """
    Reads the table with the help of the data_manager module.
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.
     Args:
        id (str): the id of the item
     Returns:
        str: the title of the item
    """
     # your code
def get_title_by_id_from_table(table, id):
     """
    Returns the title (str) of the item with the given id (str) on None om case of non-existing id.
     Args:
        table (list of lists): the sales table
        id (str): the id of the item
     Returns:
        str: the title of the item
    """
     # your code
def get_item_id_sold_last():
    """
    Reads the table with the help of the data_manager module.
    Returns the _id_ of the item that was sold most recently.
     Returns:
        str: the _id_ of the item that was sold most recently.
    """
     # your code
def get_item_id_sold_last_from_table(table):
    """
    Returns the _id_ of the item that was sold most recently.
     Args:
        table (list of lists): the sales table
     Returns:
        str: the _id_ of the item that was sold most recently.
    """
     # your code
def get_item_title_sold_last_from_table(table):
    """
    Returns the _title_ of the item that was sold most recently.
     Args:
        table (list of lists): the sales table
     Returns:
        str: the _title_ of the item that was sold most recently.
    """
     # your code
def get_the_sum_of_prices(item_ids):
    """
    Reads the table of sales with the help of the data_manager module.
    Returns the sum of the prices of the items in the item_ids.
     Args:
        item_ids (list of str): the ids
     Returns:
        number: the sum of the items' prices
    """
     # your code
def get_the_sum_of_prices_from_table(table, item_ids):
    """
    Returns the sum of the prices of the items in the item_ids.
     Args:
        table (list of lists): the sales table
        item_ids (list of str): the ids
     Returns:
        number: the sum of the items' prices
    """
     # your code
def get_customer_id_by_sale_id(sale_id):
    """
    Reads the sales table with the help of the data_manager module.
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
     Args:
         sale_id (str): sale id to search for
    Returns:
         str: customer_id that belongs to the given sale id
    """
     # your code
def get_customer_id_by_sale_id_from_table(table, sale_id):
    """
    Returns the customer_id that belongs to the given sale_id
    or None if no such sale_id is in the table.
     Args:
        table: table to remove a record from
        sale_id (str): sale id to search for
    Returns:
        str: customer_id that belongs to the given sale id
    """
     # your code
def get_all_customer_ids():
    """
    Reads the sales table with the help of the data_manager module.
     Returns:
         set of str: set of customer_ids that are present in the table
    """
     # your code
def get_all_customer_ids_from_table(table):
    """
    Returns a set of customer_ids that are present in the table.
     Args:
        table (list of list): the sales table
    Returns:
         set of str: set of customer_ids that are present in the table
    """
     # your code
def get_all_sales_ids_for_customer_ids():
    """
    Reads the customer-sales association table with the help of the data_manager module.
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
     Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
            all the sales id belong to the given customer_id
    """
     # your code
def get_all_sales_ids_for_customer_ids_form_table(table):
    """
    Returns a dictionary of (customer_id, sale_ids) where:
        customer_id:
        sale_ids (list): all the sales belong to the given customer
    (one customer id belongs to only one tuple)
    Args:
        table (list of list): the sales table
    Returns:
         (dict of (key, value): (customer_id, (list) sale_ids)) where the sale_ids list contains
         all the sales id belong to the given customer_id
    """
     # your code
def get_num_of_sales_per_customer_ids():
    """
     Reads the customer-sales association table with the help of the data_manager module.
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """
     # your code
def get_num_of_sales_per_customer_ids_from_table(table):
    """
     Returns a dictionary of (customer_id, num_of_sales) where:
        customer_id:
        num_of_sales (number): number of sales the customer made
     Args:
        table (list of list): the sales table
     Returns:
         dict of (key, value): (customer_id (str), num_of_sales (number))
    """