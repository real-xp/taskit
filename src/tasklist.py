import task as Task
import datetime
import enums

class TaskList:
    def __init__(self, name:str, tasks:list=[]):
        self.name = name
        self.tasks = tasks

    def GetName(self):
        return self.name

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

    def CreateTask(self, name:str, checked:str, priority:str, tags:str):
        checked = True if (checked in enums.YesNo.YES.value) else False
        priority = int(priority) if (0 <= int(0 if priority == "" else priority) <= 4) else enums.TaskPriority.NONE
        tags = tags.split(",")

        task = Task.Task(
            name=name,
            checked=checked,
            creationTime=datetime.datetime.now(),
            priority=priority,
            tags=tags
        )
        self.tasks.append(task)

    def DeleteTask(self, index:int):
        if (index > -1 and index < len(self.tasks)):
            del self.tasks[index]
            print(enums.PrintStatements.TASK_DELETED.value)
            return 0
        print(enums.PrintStatements.NO_TASK_FOUND.value)
        return -1

    def UpdateTask(self, index:int):
        pass

    def CheckUncheckTask(self, index:int, checked:bool=False):
        if (index > -1 and index < len(self.tasks)):
            self.tasks[index].CheckTask() if checked else self.tasks[index].UnCheckTask()
            return 0
        print(enums.PrintStatements.NO_TASK_FOUND.value)
        return -1