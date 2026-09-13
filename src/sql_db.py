import sqlite3
import enums

PATH = "test/tasks.db"

class Database:
    def __init__(self):
        self.connection = sqlite3.connect(PATH)
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.connection.row_factory = sqlite3.Row
        self._CreateTable()

    def _CreateTable(self):
        cursor = self.connection.cursor()
        cursor.execute(enums.DBQueries.CREATE_TASKLISTS.value)
        cursor.execute(enums.DBQueries.CREATE_TASK.value)
        self.connection.commit()

    def CreateTaskList(self, name:str, creationDate:str):
        cursor = self.connection.cursor()
        cursor.execute(enums.DBQueries.CREATE_TASKLIST_ENTRY.value, (name, creationDate))
        self.connection.commit()
        return cursor.lastrowid

    def CreateTask(self, tasklistID:str, name:str, checked:int, priority:int, creationDate, tags:str):
        cursor = self.connection.cursor()
        cursor.execute(enums.DBQueries.CREATE_TASK_ENTRY.value, (tasklistID, name, checked, priority, creationDate, tags))
        self.connection.commit()
        return cursor.lastrowid

    def LoadTaskLists(self):
        cursor = self.connection.cursor()
        cursor.execute(enums.DBQueries.LOAD_ALL_TASKLISTS.value)
        return cursor.fetchall()

    def LoadTaskInTasklist(self, tasklistID):
        cursor = self.connection.cursor()
        cursor.execute(enums.DBQueries.LOAD_ALL_TASKS.value, (tasklistID, ))
        return cursor.fetchall()

    def DropAllTables(self, makeNewTable:bool=False):
        cursor = self.connection.cursor()
        cursor.execute(enums.DBQueries.DELETE_ALL_TASKS.value)
        cursor.execute(enums.DBQueries.DELETE_ALL_TASKLISTS.value)
        self.connection.commit()
        if (makeNewTable): self._CreateTable()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type is not None: self.connection.rollback()
        else: self.connection.commit()
        self.connection.close()
        return False