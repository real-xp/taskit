# Imports
import sqlite3
import enums

# CONSTANTS
PATH = "test/tasks.db"

# Main database class.
class Database:

    # Basically initializes the database.
    # Makes sure every row is a sqlite row object.
    # also make sures foreign keys are on for relational tables.
    def __init__(self):
        self.connection = sqlite3.connect(PATH)
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.connection.row_factory = sqlite3.Row
        self._CreateTable()

    # ---------------------------------------

    # Creates the tables if they exist for tasklist and tasks.
    def _CreateTable(self) -> None:
        cursor = self.connection.cursor()
        cursor.execute(enums.DBQueries.CREATE_TASKLISTS.value)
        cursor.execute(enums.DBQueries.CREATE_TASK.value)
        self.connection.commit()

    # ---------------------------------------

    # Creates the task list entry and returns its rowid.
    def CreateTaskList(self, name:str, creationDate:str) -> int | None:
        cursor = self.connection.cursor()
        cursor.execute(enums.DBQueries.CREATE_TASKLIST_ENTRY.value, (name, creationDate))
        self.connection.commit()
        return cursor.lastrowid

    # ---------------------------------------

    # Creates the task entry based on the tasklistID and returns its rowid.
    def CreateTask(self, tasklistID:str, name:str, checked:int, priority:int, creationDate, tags:str) -> int | None:
        cursor = self.connection.cursor()
        cursor.execute(enums.DBQueries.CREATE_TASK_ENTRY.value, (tasklistID, name, checked, priority, creationDate, tags))
        self.connection.commit()
        return cursor.lastrowid

    # ---------------------------------------

    # Loads the task list entry and returns a SQLiteRowObject list
    def LoadTaskLists(self) -> list:
        cursor = self.connection.cursor()
        cursor.execute(enums.DBQueries.LOAD_ALL_TASKLISTS.value)
        return cursor.fetchall()

    # ---------------------------------------

    # Loads the task entry based on the tasklistID and returns a SQLiteRowObject list
    def LoadTaskInTasklist(self, tasklistID) -> list:
        cursor = self.connection.cursor()
        cursor.execute(enums.DBQueries.LOAD_ALL_TASKS.value, (tasklistID, ))
        return cursor.fetchall()

    # ---------------------------------------

    # Deletes all the tables.
    # Also has an option of if we want to make a new table.
    def DropAllTables(self, makeNewTable:bool=False) -> None:
        cursor = self.connection.cursor()
        cursor.execute(enums.DBQueries.DELETE_ALL_TASKS.value)
        cursor.execute(enums.DBQueries.DELETE_ALL_TASKLISTS.value)
        self.connection.commit()
        if (makeNewTable): self._CreateTable()

    # ---------------------------------------

    # For safe entry into the database
    def __enter__(self):
        return self

    # ---------------------------------------

    # For safe exit out of database.
    # If note, it will roll back the changes made.
    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None: self.connection.rollback()
        else: self.connection.commit()
        self.connection.close()
        return False