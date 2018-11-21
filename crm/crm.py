""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
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

    table = data_manager.get_table_from_file("crm/customers_test.csv")
    options = (["Show table",
                "Add to table",
                "Remove from table",
                "Update table",
                "Get longest name ID",
                "Get subscribed e-mails"])
    while True:
        ui.print_menu("Customer Relationship management", options, "Back to main manu")
        inputs = ui.get_inputs(["Please enter a number"], "")
        option = inputs[0]
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            input_id = ui.get_inputs(["ID"], "Choose an ID to remove")
            remove(table, input_id)
        elif option == "4":
            input_id = ui.get_inputs(["ID"], "Choose an ID to update")
            update(table, id_)
        elif option == "5":
            get_longest_name_id(table)
        elif option == "6":
            get_subscribed_emails(table)
        elif option == "0":
            break


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    titles = ["ID", "Name", "Email", "Subscribed"]
    ui.print_table(table, titles)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    new_data = []
    new_data.append(common.generate_random(table))
    new_data.extend(ui.get_inputs(["Name", "Email", "Subscribed"], "Please provide the necessary information"))
    table.append(new_data)
    data_manager.write_table_to_file("crm/customers_test.csv", table)
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
    wrong_id = True
    while wrong_id:
        for row in table:
            if row[0] == id_[0]:
                table.remove(row)
                wrong_id = False
    data_manager.write_table_to_file("crm/customers_test.csv", table)
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
        for row in table:
            if row[0] == id_[0]:
                table[id_index] = ui.get_inputs(["Name", "Email", "Subscribed"], "Please provide the necessary information")
                table[id_index].insert(0, id_[0])
                wrong_id = False
            else:
                id_index += 1
    data_manager.write_table_to_file("crm/customers_test.csv", table)
    return table


# special functions:
# ------------------

def get_longest_name_id(table):
    """
        Question: What is the id of the customer with the longest name?

        Args:
            table (list): data table to work on

        Returns:
            string: id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
        """

    longest_name_lenght = 0
    longest_name_id = ""
    longest_names = []
    for row in table:
        if len(row[1]) > longest_name_lenght:
            longest_name_lenght = len(row[1])
    for row in table:
        if len(row[1]) == longest_name_lenght:
            longest_names.append(row[1])
    common.abc_order(longest_names)
    for row in table:
        if longest_names[-1] in row:
            longest_name_id = row[0]
    ui.print_result(longest_name_id, "The longest name's ID is")
    return longest_name_id


def get_subscribed_emails(table):
    """
        Question: Which customers has subscribed to the newsletter?

        Args:
            table (list): data table to work on

        Returns:
            list: list of strings (where a string is like "email;name")
        """

    emails_and_names = ""
    for row in table:
        if row[-1] == "1":
            emails_and_names += (row[-2] + ";" + row[1] + ",")
    emails_and_names = emails_and_names.strip(",")
    emails_and_names = emails_and_names.split(",")
    ui.print_result(list(emails_and_names), "The data list is")
    return list(emails_and_names)

    # your code


# functions supports data analyser
# --------------------------------


def get_name_by_id(id):
    """
    Reads the table with the help of the data_manager module.
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    # your code



def get_name_by_id_from_table(table, id):
    """
    Returns the name (str) of the customer with the given id (str) on None om case of non-existing id.

    Args:
        table (list of lists): the customer table
        id (str): the id of the customer

    Returns:
        str: the name of the customer
    """

    # your code
