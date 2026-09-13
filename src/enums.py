from enum import Enum

_LINE_STAR_COUNT = 100
_LINE_STAR_COUNT_BIG = 150

class DBQueries(Enum):
    CREATE_TASKLISTS = '''
CREATE TABLE IF NOT EXISTS tasklists (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    creationDate TEXT DEFAULT CURRENT_TIMESTAMP
)
'''

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

    CREATE_TASKLIST_ENTRY = '''
INSERT INTO tasklists (name, creationDate) VALUES (?, ?)
'''

    CREATE_TASK_ENTRY = '''
INSERT INTO tasks (tasklistID, name, checked, priority, creationDate, tags) VALUES (?, ?, ?, ?, ?, ?)
'''

    LOAD_ALL_TASKLISTS = '''
SELECT * FROM tasklists ORDER BY id
'''

    LOAD_ALL_TASKS = '''
SELECT * FROM tasks WHERE tasklistID = ? ORDER BY id
'''

    DELETE_ALL_TASKS = '''
DROP TABLE IF EXISTS tasks
'''

    DELETE_ALL_TASKLISTS = '''
DROP TABLE IF EXISTS tasklists
'''

class YesNo(Enum):
    YES = ('yes', 'y', 'ye')
    NO = ('no', 'n')

class Menu(Enum):
    MAIN_MENU = 0
    IN_TASK_LIST = 1

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

class TaskPriority(Enum):
    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    MAXIMUM = 4

class PrintStatements(Enum):
    MAIN_MENU_HELP = f'''
{"-"*_LINE_STAR_COUNT}
TASKIT
{"-"*_LINE_STAR_COUNT}

Welcome to TaskIt! This app allows you to manage tasks and task lists.
You are currently in the MAIN MENU.

To see all the lists, when prompted, type - "lists"
To access a list, when prompted, type - "view;<name>" or "open;<name>" without <>
To create a list, when prompted, type - "create" or "create;<name>" without <>
To delete a list, when prompted, type - "delete" or "delete;<name>" without <>

To see this message again, or see help page on any menu, when prompted, type - "help"
To quit, when prompted, type "exit" or "quit"

{"-"*_LINE_STAR_COUNT}
'''

    IN_TASK_LIST_HELP = f'''
{"-"*_LINE_STAR_COUNT}
TASKIT
{"-"*_LINE_STAR_COUNT}

You are in a Task List.

To see all the tasks, when prompted, type - "view"
To create a task, when prompted, type - "create" or "create;<name>" without <>
    When asked about checked, type 'y' for yes or 'n' for no
    When asked about priority, type 0 (None) or 1 (Low) or 2 (Medium) or 3 (High) or 4 (Maximum)
    When asked about tags, type the tags followed by a single `,` (no space after `,`)
To update a task, when prompted, type - "update;<name>" without <>
To delete a task, when prompted, type - "delete" or "delete;<name>" or or "delete;<index>" without <>

To see this message again, or see help page on any menu, when prompted, type - "help"
To quit, when prompted, type "exit" or "quit"

{"-"*_LINE_STAR_COUNT}
'''
    
    EXIT_STATEMENT = f'''
{"-"*_LINE_STAR_COUNT}
Thank You For Using TaskIt.
{"-"*_LINE_STAR_COUNT}
'''

    NO_TASK_LIST_EXIST = f'''
{"-"*_LINE_STAR_COUNT}
No Task Lists Exist! Create A New One Using "create" or "create;<name-of-task-list>"
{"-"*_LINE_STAR_COUNT}
'''

    NEW_TASK_LIST_CREATED = f'''
{"-"*_LINE_STAR_COUNT}
New Task List Created!
{"-"*_LINE_STAR_COUNT}
'''
    
    TASK_LIST_DELETED = f'''
{"-"*_LINE_STAR_COUNT}
Task List Has Been Deleted!
{"-"*_LINE_STAR_COUNT}
'''

    TASK_LIST_UPDATED = f'''
{"-"*_LINE_STAR_COUNT}
Task List Has Been Updated!
{"-"*_LINE_STAR_COUNT}
'''
    
    NO_TASK_FOUND = f'''
{"-"*_LINE_STAR_COUNT}
No Task Found! Create A New One Using "create" or "create;<name-of-task>"
{"-"*_LINE_STAR_COUNT}
'''

    TASK_DELETED = f'''
{"-"*_LINE_STAR_COUNT}
Task Has Been Deleted!
{"-"*_LINE_STAR_COUNT}
'''

    TASK_UPDATED = f'''
{"-"*_LINE_STAR_COUNT}
Task Has Been Updated!
{"-"*_LINE_STAR_COUNT}
'''

    RETURNING_TO_MAIN_MENU = f'''
{"-"*_LINE_STAR_COUNT}
Returning To Main Menu!
{"-"*_LINE_STAR_COUNT}
'''

    SAVED_SUCCESSFULLY = f'''
{"-"*_LINE_STAR_COUNT}
Data Saved Successfully!
{"-"*_LINE_STAR_COUNT}
'''
