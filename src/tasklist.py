# Imports
import task as Task
import datetime
import enums

# Class to create a tasklist.
class TaskList:

    # Initializer for the class.
    # Creates a task list.
    def __init__(self, name:str, tasks:list=[], creationDate=datetime.datetime.now()):
        self.name = name
        self.creationDate = creationDate
        self.tasks = tasks

    # ---------------------------------------

    # Prints the header for the task list information, object independent.
    def ShowTaskListInfo_Header(cls):
        print("-"*enums._LINE_STAR_COUNT_BIG)
        print(f"{"UID":3} {" ":10} {"Task List Name":40} {"Total Tasks":10}")
        print("-"*enums._LINE_STAR_COUNT_BIG)

    # ---------------------------------------

    # Prints the task list information.
    def ShowTaskListInfo(self):
        print(f"{self.name:40} {len(self.tasks):10}")

    # ---------------------------------------

    # Generic functions to return attribute names.
    def GetName(self): return self.name
    def GetCreationDate(self): return str(self.creationDate)
    def GetTasks(self): return self.tasks if len(self.tasks) > 0 else None

    # ---------------------------------------

    # Generic functions to update name.
    def UpdateName(self, name:str):
        if (name != ""): self.name = name

    # ---------------------------------------

    # Function that prints all tasks in the current tasklist object.
    def ShowTasks(self):
        tasks = self.GetTasks()
        if (tasks is not None):
            tasks[0].ShowTaskInfo_Header()

            for i in range(len(tasks)):
                print(f"{i:3} {" ":10} ", end="")
                tasks[i].ShowTaskInfo()

        print("-"*enums._LINE_STAR_COUNT_BIG)

    # ---------------------------------------

    # Function to create a new task.
    # Has incorrect type checking.
    # Allows for flexibility of parameters.
    def CreateTask(self, name:str, checked:str, priority:str, tags:str, creationDate=""):
        checked = True if (checked in enums.YesNo.YES.value) else False

        priority = str(priority)
        if priority == "" or priority.isalpha() or priority.isalnum(): priority = 0
        priority = int(priority) if (0 <= priority <= 4) else enums.TaskPriority.NONE
        
        tags = tags.split(",")

        task = Task.Task(
            name=name,
            checked=checked,
            priority=priority,
            tags=tags,
        )
        if (creationDate != ""): task.SetCreationDate(date=creationDate)

        self.tasks.append(task)

    # ---------------------------------------

    # Deletes a task from a list if it exists within the given index.
    def DeleteTask(self, index:int):
        if (index > -1 and index < len(self.tasks)):
            del self.tasks[index]
            print(enums.PrintStatements.TASK_DELETED.value)
            return 0
        
        print(enums.PrintStatements.NO_TASK_FOUND.value)
        return -1

    # ---------------------------------------

    # Updates a task from a list if it exists within the given index.
    def UpdateTask(self, index:int, name:str="", priority:int=enums.TaskPriority.NONE, tags:list=[], checked:bool=False):
        if (index > -1 and index < len(self.tasks)):
            self.tasks[index].UpdateFields(name=name, priority=priority, tags=tags, checked=checked)
            print(enums.PrintStatements.TASK_UPDATED.value)
            return 0
        
        print(enums.PrintStatements.NO_TASK_FOUND.value)
        return -1
    
    # ---------------------------------------

    # Checks Or Unchecks a task from a list if it exists within the given index.
    def CheckUncheckTask(self, index:int, checked:bool=False):
        if (index > -1 and index < len(self.tasks)):
            self.tasks[index].CheckTask() if checked else self.tasks[index].UnCheckTask()
            print(enums.PrintStatements.TASK_UPDATED.value)
            return 0
        
        print(enums.PrintStatements.NO_TASK_FOUND.value)
        return -1