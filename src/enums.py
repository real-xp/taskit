# Imports
from enum import Enum

# ---------------------------------------

# CONSTANTS
_LINE_STAR_COUNT = 100
_LINE_STAR_COUNT_BIG = 150
APPNAME = "TaskIt"

# ---------------------------------------

# Enum for SQLite queries.
class DBQueries(Enum):

    # Creates a new table for Tasklists
    CREATE_TASKLISTS = '''
CREATE TABLE IF NOT EXISTS tasklists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    creationDate TEXT DEFAULT CURRENT_TIMESTAMP
)
'''

    # Creates a new table for tasks linked using primary keys with tasklists
    CREATE_TASK = '''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tasklistID INTEGER NOT NULL,
    name TEXT NOT NULL,
    checked INTEGER NOT NULL DEFAULT 0,
    priority INTEGER NOT NULL DEFAULT 0,
    creationDate TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    tags TEXT,
    FOREIGN KEY (tasklistID) REFERENCES tasklists(id) ON DELETE CASCADE
)
'''

    # Creates a new tasklist entry
    CREATE_TASKLIST_ENTRY = '''
INSERT INTO tasklists (name, creationDate) VALUES (?, ?)
'''

    # Creates a new task entry
    CREATE_TASK_ENTRY = '''
INSERT INTO tasks (tasklistID, name, checked, priority, creationDate, tags) VALUES (?, ?, ?, ?, ?, ?)
'''

    # Loads all tasklists
    LOAD_ALL_TASKLISTS = '''
SELECT * FROM tasklists ORDER BY id
'''

    # Loads all tasks from a particular tasklistID
    LOAD_ALL_TASKS = '''
SELECT * FROM tasks WHERE tasklistID = ? ORDER BY id
'''

    # Deletes all tasklists.
    DELETE_ALL_TASKLISTS = '''
DROP TABLE IF EXISTS tasklists
'''

    # Deletes all tasks.
    DELETE_ALL_TASKS = '''
DROP TABLE IF EXISTS tasks
'''

# ---------------------------------------

# Enum for Yes Or No arguments.
# No idea why i made this?
class YesNo(Enum):
    YES = ('yes', 'y', 'ye')
    NO = ('no', 'n')

# ---------------------------------------

# Enum for Menu management.
class Menu(Enum):
    MAIN_MENU = 0
    IN_TASK_LIST = 1

# ---------------------------------------

# Enum for argument parse management.
# Each entry here is a tuple so we can use membership operators to see if user wrote one of the options.
class Args(Enum):
    HELP = ("help", "h")
    MAIN = ("main", "home")
    CREATE = ("create")
    DELETE = ("delete")
    CLEAR = ("clear", "clean", "", " ")
    CHECK = ("check", "tick")
    UNCHECK = ("uncheck", "untick", "cross")
    UPDATE = ("update")
    OPEN = ("open")
    VIEW = ("view")
    SAVE = ("save")
    LISTS = ("lists", "view-lists", "view")
    EXIT = ("exit", "quit", "q", "leave")

# ---------------------------------------

# Enum for task priority
class TaskPriority(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    MAXIMUM = 4

# ---------------------------------------

# Enum to show all print statements that are static for most part
class PrintStatements(Enum):

    # Prints the main menu help text.
    MAIN_MENU_HELP = f'''
{"-"*_LINE_STAR_COUNT}
{APPNAME}
{"-"*_LINE_STAR_COUNT}

Welcome to {APPNAME}! This app allows you to manage tasks and task lists.
You are currently in the MAIN MENU.

To see all the lists, when prompted, type - "view" or "lists"
To create a list, when prompted, type - "create" or "create;<name>" without <>
To access a list, when prompted, type - "open;<name>" without <>
To update a list, when prompted, type - "update;<name>;<new name>" or "update" without <>
To delete a list, when prompted, type - "delete" or "delete;<name>" without <>

To save the database into a '.db' file, type "save" when prompted.
To go back to the main menu, type "home" when prompted.

To see this message again, or see help page on any menu, when prompted, type - "help"
To quit, when prompted, type "exit" or "quit"

{"-"*_LINE_STAR_COUNT}
'''

    # Prints the tasklist help text.
    IN_TASK_LIST_HELP = f'''
{"-"*_LINE_STAR_COUNT}
{APPNAME}
{"-"*_LINE_STAR_COUNT}

You are in a Task List.

To create a task, when prompted, type - "create" or "create;<name>" without <>
    When asked about checked, type 'y' for yes or 'n' for no
    When asked about priority, type 0 (None) or 1 (Low) or 2 (Medium) or 3 (High) or 4 (Maximum)
    When asked about tags, type the tags followed by a single `,` (no space after `,`)
To see all the tasks, when prompted, type - "view"
To update a task, when prompted, type - "update;<index>" without <>
To delete a task, when prompted, type - "delete" or "delete;<index>" or without <>
To check or uncheck a task, when prompted, type - "check;<index>" or "uncheck;<index>" without <>

To save the database into a '.db' file, type "save" when prompted.
To go back to the main menu, type "home" when prompted.

To see this message again, or see help page on any menu, when prompted, type - "help"
To quit, when prompted, type "exit" or "quit"

{"-"*_LINE_STAR_COUNT}
'''
    
    # Prints the exit text.
    EXIT_STATEMENT = f'''
{"-"*_LINE_STAR_COUNT}
Thank You For Using {APPNAME}.
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the invalid input text.
    INVALID_STATEMENT = f'''
{"-"*_LINE_STAR_COUNT}
Invalid statement. Please refer to help page for valid options.
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the error text.
    MAJOR_ERROR_STATEMENT = f'''
{"-"*_LINE_STAR_COUNT}
Unknown error has occured. The program will now exit.
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the no tast list found text.
    NO_TASK_LIST_EXIST = f'''
{"-"*_LINE_STAR_COUNT}
No Task Lists Exist! Create A New One Using "create" or "create;<name-of-task-list>"
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the tast list does not exists text.
    NO_TASK_LIST_EXIST_SIMPLE = f'''
{"-"*_LINE_STAR_COUNT}
Error - Task List Does Not Exist!
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the tast list created text.
    NEW_TASK_LIST_CREATED = f'''
{"-"*_LINE_STAR_COUNT}
New Task List Created!
{"-"*_LINE_STAR_COUNT}
'''
    
    # Prints the tast list already exists text.
    TASK_LIST_ALREADY_EXISTS = f'''
{"-"*_LINE_STAR_COUNT}
Error - Task List Already Exists!
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the tast list already exists other text.
    TASK_LIST_ALREADY_EXISTS_OTHER = f'''
{"-"*_LINE_STAR_COUNT}
Error - Task List With That Name Already Exists!
{"-"*_LINE_STAR_COUNT}
'''
    
    # Prints the tast list deleted text.
    TASK_LIST_DELETED = f'''
{"-"*_LINE_STAR_COUNT}
Task List Has Been Deleted!
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the tast list cannot have no name text.
    TASK_LIST_NOT_EMPTY_NAME = f'''
{"-"*_LINE_STAR_COUNT}
Error - Task List Name Cannot Be Empty!
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the tast list updated text.
    TASK_LIST_UPDATED = f'''
{"-"*_LINE_STAR_COUNT}
Task List Has Been Updated!
{"-"*_LINE_STAR_COUNT}
'''
    
    # Prints the no tast found text.
    NO_TASK_FOUND = f'''
{"-"*_LINE_STAR_COUNT}
No Task Found! Create A New One Using "create" or "create;<name-of-task>"
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the tast created text.
    TASK_CREATED = f'''
{"-"*_LINE_STAR_COUNT}
Task Has Been Created!
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the tast deleted text.
    TASK_DELETED = f'''
{"-"*_LINE_STAR_COUNT}
Task Has Been Deleted!
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the tast updated text.
    TASK_UPDATED = f'''
{"-"*_LINE_STAR_COUNT}
Task Has Been Updated!
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the home menu return text.
    RETURNING_TO_MAIN_MENU = f'''
{"-"*_LINE_STAR_COUNT}
Returning To Main Menu!
{"-"*_LINE_STAR_COUNT}
'''

    # Prints the successful save text.
    SAVED_SUCCESSFULLY = f'''
{"-"*_LINE_STAR_COUNT}
Data Saved Successfully!
{"-"*_LINE_STAR_COUNT}
'''

# Unused Leftover
class PyQt6StyleSheet(Enum):
    STYLESHEET = """
    QPushButton#AddTaskListButton, QPushButton#AddTaskButton {
        border-radius: 10px;
        background-color: #AAFFAA;
        padding: 24px;
        font-size: 32px;
        font-family: "Rubik";
    }

    QPushButton#DeleteTaskListButton {
        border-radius: 10px;
        background-color: #FFAAAA;
        padding: 24px;
        font-size: 32px;
        font-family: "Rubik";
    }

    QLabel#sideBarHeaderTitle{
        font-size: 15px;
        font-family: "Rubik";
        font-weight: 600;
    }

    QLabel#mainBarHeaderTitle{
        font-size: 15px;
        font-family: "Rubik";
        font-weight: 600;
    }

    QWidget#TaskListEntry{
        border-radius: 10px;
        background-color: #FFF;
        padding: 20px;
        font-family: "Rubik";
    }

    QWidget#TaskEntry{
        border-radius: 10px;
        background-color: #FFF;
        padding: 15px;
        font-family: "Rubik";
    }

    QWidget#TaskListEntryButton{
        border-radius: 10px;
        background-color: #DDD;
        padding: 10px 20px 10px 20px;
        font-family: "Rubik";
    }

    QWidget#TaskDeleteButton{
        border-radius: 10px;
        background-color: #FFAAAA;
        padding: 10px 20px 10px 20px;
        font-family: "Rubik";
    }

    QPushButton#TaskListEntryButton:hover {
        background-color: #F8F8F8;
    }

    QPushButton#TaskListEntryButton:pressed {
        background-color: #F0F0F0;
    }

    QLabel#TitleCardObject {
        font-size: 32px;
        font-family: "Rubik";
        font-weight: 600;
    }

    QLabel#FieldNameTitle {
        font-size: 16px;
        font-family: "Rubik";
        font-weight: 400;
    }

    QPushButton#SaveButtonWidget {
        border-radius: 10px;
        background-color: #FFAAAA;
        padding: 8px;
        font-size: 18px;
        font-family: "Rubik";
    }
    """