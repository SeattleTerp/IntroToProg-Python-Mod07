# ------------------------------------------------- #
# Title: Assignment07
# Description: A simple example of storing data in a binary file
#              while exhibiting structured error handling
# ChangeLog: (Who, When, What)
# <RKramer>,<5.24.2021>,Created Script
# <RKramer>,<5.25.2021>,Imported Assignment06 script
# <RKramer>,<5.25.2021>,Added combined binary read and write function
# <RKramer>,<5.25.2021>,Modified add and remove data functions
# <RKramer>,<5.26.2021>,Added exception clauses to manage file function
# <RKramer>,<5.26.2021>,Added exception clauses to I/O class
# ------------------------------------------------- #

import pickle #This imports code from another code file

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
file_name = "ToDoList.dat"  # The name of the data file
objFile = "ToDoList.dat"  # An object that represents a file
row = {}  # A row of data separated into elements of a dictionary {Task,Priority}
list_of_rows = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strStatus = ""  # Captures the status of an processing functions

# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def manage_file(file_name, mode, data=None):
        """ A custom wrapper function for the standard open() file function

        :param data: (string) with data to save
        :param file_name: (string) with name of file
        :param mode: (string) with name of mode [Write,Overwrite,Read]
        :return: (string) with data or write/append status
        """
        return_data = []
        if mode.lower() == 'append':
            with open(file_name, "ab+") as file:
                pickle.dump(list_of_rows, file)
                return_data = 'New data added to file!'
        elif mode.lower() == 'overwrite':
            with open(file_name, "wb+") as file:
                for row in list_of_rows:
                    pickle.dump(row, file)
                    return_data = 'File overwritten and new data added to file!'
        elif mode.lower() == 'read':
            with open(file_name, "rb+") as file:
                try:
                    cnt = 0
                    for cnt in range(1000):
                        row = pickle.load(file)
                        list_of_rows.append(row) #Load() only loads one row of data
                        cnt += 1
                except EOFError as e:
                        e #Will Always bring up error as long as table does not exceed 1000 objects
        elif mode.lower() == 'reload':
            list_of_rows.clear()
            with open(file_name, "rb+") as file:
                try:
                    cnt = 0
                    for cnt in range(1000):
                        row = pickle.load(file)
                        list_of_rows.append(row) #Load() only loads one row of data
                        cnt += 1
                except EOFError as e:
                        e #Will Always bring up error as long as table does not exceed 1000 objects
        else:
            return_data = "No matching mode option"
        return return_data

    @staticmethod
    def add_data_to_list(task, priority, list_of_rows):
        """ Adds data to a list of dictionary rows

        :param task: (string) with name of task:
        :param priority: (string) with priority level:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        row = [{"Task": str(task).strip(), "Priority": str(priority).strip()}]
        list_of_rows.append(row)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task_to_remove, list_of_rows):
        """ Removes task data and associated priority from list of dictionary rows

        :param task_to_remove: (string) with name of task to be removed:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        for row in list_of_rows:
            for item in row:
                if item["Task"].lower() == task_to_remove.lower():
                    list_of_rows.remove(row)
                    print("row removed")
        return list_of_rows, 'Success'

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Overwrite Data to File     
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks To Do are: *******")
        # print(list_of_rows)
        for row in list_of_rows:
            row_print = row
            print(str(row_print)[2:-2])
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Asks for new task and task's priority

        :return: (strings) of task and priority
        """
        try:
            task = str(input("Task:")).strip()
            priority = str(input("Priority:")).strip()
            if priority.lower != "High" or "Medium" or "Low":
                raise Exception('Priority must be High, Medium or Low')
        except Exception as e:
            print("There was an input error")
            print(e)
            print()
            task = str(input("Task:")).strip()
            priority = str(input("Priority:")).strip()
        return task, priority

    @staticmethod
    def input_task_to_remove():
        """ Asks for task to remove

        :return: (strings) of task to remove
        """
        task_to_remove = str(input("Which task would you like to remove:")).strip()
        print()
        return task_to_remove


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoList.dat.
print('Here is the current data from the file:')
Processor.manage_file(file_name, mode='read')
#print(Processor.manage_file(file_name, mode='read')) # read file data

# Step 2 - Display a menu of choices to the user
while (True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(list_of_rows)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        task, priority = IO.input_new_task_and_priority()
        Processor.add_data_to_list(task, priority, list_of_rows)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        task_to_remove = IO.input_task_to_remove()
        Processor.remove_data_from_list(task_to_remove, list_of_rows)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':  # Overwrite Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.manage_file(file_name, mode='overwrite')
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.manage_file(file_name, mode='reload')
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload  Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break  # and Exit