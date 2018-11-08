""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
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
    table = data_manager.get_table_from_file("hr/persons_test.csv")
    options = (["Show table",
                "Add to table",
                "Remove from table",
                "Update the table",
                "Get oldest person",
                "Get person close to avarage"])
    ui.print_menu("HR menu", options, "Back to main menu")
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
        get_oldest_person(table)
    elif option == "6":
        get_persons_closest_to_average(table)
    elif option == "0":
        pass                       #ui.print_menu("Main menu", options, "Exit program")
    else:
        raise KeyError("There is no such option.")

    # your code"""


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """
    title_list = ["ID", "Name", "Year"]
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

    title_list = ["Name: ", "Year: "]
    inputs = [] 
    id_ = common.generate_random(table)
    inputs.extend(ui.get_inputs(title_list, "Please provide the required information:"))
    inputs.insert(0,id_)
    table.append(inputs)
    data_manager.write_table_to_file("hr/persons_test.csv", table)
    start_module()
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
    inputs.extend(ui.get_inputs(title_list, "ID of removable person:"))
    for lst in table:
        if inputs[0] in lst:
            table.remove(lst)
    data_manager.write_table_to_file("hr/persons_test.csv", table)
    start_module()
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
    wrong_id = True
    while wrong_id:
        id_ = ui.get_inputs(["ID: "], "Choose an ID to update: ")
        for row in table:
            if row[0] == id_[0]:
                table[id_index] = ui.get_inputs(["Name: ", "Year: "], "Please provide the necessary information: ")
                inputs(["Name: ","Year: "], "Please provide the necessary information: ")
                table[id_index].insert(0, id_[0])
                wrong_id = False
            else:
                id_index += 1
    data_manager.write_table_to_file("hr/persons_test.csv", table)
    start_module()
    return table

# special functions:
# ------------------

def get_oldest_person(table):
    """
    Question: Who is the oldest person?

    Args:
        table (list): data table to work on

    Returns:
        list: A list of strings (name or names if there are two more with the same value)
    """

    # your code
    year_of_oldest = 2180
    name_of_oldest = []
    for lst in table:
        a = int(lst[2])
        if year_of_oldest > a:
            year_of_oldest = a
    for lst in table:
        year_of_oldest = str(year_of_oldest)
        if year_of_oldest in lst:
            name_of_oldest.append(lst[0])
    ui.print_result(name_of_oldest, "Oldest Person: ")




def get_persons_closest_to_average(table):
    """
    Question: Who is the closest to the average age?

    Args:
        table (list): data table to work on

    Returns:
        list: list of strings (name or names if there are two more with the same value)
    """
    avarage_of_years = 0
    name_of_avarage = []
    smallest_diff = 100
    for lst in table:
        a = int(lst[2])
        avarage_of_years += a
    avarage_of_years = round(avarage_of_years / len(table))
    for lst in table:
        if avarage_of_years in lst:
            name_of_avarage.append(lst[1])
        elif avarage_of_years not in lst:
            diff = int(lst[2]) - avarage_of_years
            if diff < 0:
                diff = diff * -1 
            if diff < smallest_diff:
                smallest_diff = diff
    for lst in table:
        smallest_diff_neg = str(avarage_of_years - smallest_diff)
        smallest_diff_poz = str(avarage_of_years + smallest_diff)
        if (smallest_diff_neg or smallest_diff_poz) in lst:
            name_of_avarage.append(lst[1])
    ui.print_result(name_of_avarage, "Person(s) closest to avarage")


    # your code
