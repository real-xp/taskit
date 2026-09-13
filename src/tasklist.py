import task as Task
import datetime
import enums
import sql_db

class TaskList:
    def __init__(self, name:str, tasks:list=[], creationDate=datetime.datetime.now()):
        # self.id = ""
        self.name = name
        self.creationDate = creationDate
        self.tasks = tasks
        # with sql_db.Database() as db:
        #     self.id = db.CreateTaskList(name=name, creationDate=str(self.creationDate))

    def ShowTaskListInfo_Header(cls):
        print("-"*enums._LINE_STAR_COUNT_BIG)
        print(f"{"UID":3} {" ":10} {"Task List Name":40} {"Total Tasks":10}")
        print("-"*enums._LINE_STAR_COUNT_BIG)

    def ShowTaskListInfo(self):
        print(f"{self.name:40} {len(self.tasks):10}")

    def GetName(self):
        return self.name

    def GetCreationDate(self):
        return str(self.creationDate)

    def UpdateName(self, name:str):
        if (name != ""):
            self.name = name

    def GetTasks(self):
        return self.tasks if len(self.tasks) > 0 else None

    def ShowTasks(self):
        tasks = self.GetTasks()
        if (tasks is not None):
            tasks[0].ShowTaskInfo_Header()
            for i in range(len(tasks)):
                print(f"{i:3} {" ":10} ", end="")
                tasks[i].ShowTaskInfo()
        print("-"*enums._LINE_STAR_COUNT_BIG)

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

    def DeleteTask(self, index:int):
        if (index > -1 and index < len(self.tasks)):
            del self.tasks[index]
            print(enums.PrintStatements.TASK_DELETED.value)
            return 0
        print(enums.PrintStatements.NO_TASK_FOUND.value)
        return -1

    def UpdateTask(self, index:int, name:str="", priority:int=enums.TaskPriority.NONE, tags:list=[], checked:bool=False):
        if (index > -1 and index < len(self.tasks)):
            self.tasks[index].UpdateFields(name=name, priority=priority, tags=tags, checked=checked)
            print(enums.PrintStatements.TASK_UPDATED.value)
            return 0
        print(enums.PrintStatements.NO_TASK_FOUND.value)
        return -1
    
    def CheckUncheckTask(self, index:int, checked:bool=False):
        if (index > -1 and index < len(self.tasks)):
            self.tasks[index].CheckTask() if checked else self.tasks[index].UnCheckTask()
            return 0
        print(enums.PrintStatements.NO_TASK_FOUND.value)
        return -1