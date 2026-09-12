import datetime
import enums

class Task:
    def __init__(self, name:str, checked:bool, creationTime:str, priority:int=enums.TaskPriority.NONE, tags:list=[]):
        self.name = name
        self.checked = checked
        self.creationTime = creationTime
        self.checkedDate = ""
        self.priority = priority
        self.tags = tags

    def ShowTaskInfo_Header(cls):
        print("-"*enums._LINE_STAR_COUNT_BIG)
        print(f"{"UID":3} {" ":10} {"Task Name":30} {"Checked":20} {"Creation Date":30} {"Priority":20} Tags")
        print("-"*enums._LINE_STAR_COUNT_BIG)

    def ShowTaskInfo(self):
        print(f"{self.name:30} {"Yes" if self.checked else "No":20} {str(self.creationTime):30} {enums.TaskPriority(self.priority).name:20} {self.tags}")

    def SetPriority(self, priority:int=enums.TaskPriority.NONE):
        self.priority = priority

    def SetTags(self, tags:list=[]):
        self.tags.extend(tags)

    def CheckTask(self):
        self.checked = True
        self.checkedDate = datetime.datetime.now()

    def UnCheckTask(self):
        self.checked = False
        self.checkedDate = ""
