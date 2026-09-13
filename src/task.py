import datetime
import enums
import sql_db

class Task:
    def __init__(self, name:str, checked:bool, creationTime=datetime.datetime.now(), priority:int=enums.TaskPriority.NONE, tags:list=[]):
        # self.id = ""
        self.name = name
        self.checked = checked
        self.creationTime = creationTime
        self.checkedDate = ""
        self.priority = priority
        self.tags = tags
        # with sql_db.Database() as db:
        #     self.id = db.CreateTask(name=name, checked=int(checked), tags=str(tags), priority=priority, tasklistID=tasklistID, creationDate=str(self.creationDate))

    def ShowTaskInfo_Header(cls):
        print("-"*enums._LINE_STAR_COUNT_BIG)
        print(f"{"UID":3} {" ":10} {"Task Name":30} {"Checked":20} {"Creation Date":30} {"Priority":20} Tags")
        print("-"*enums._LINE_STAR_COUNT_BIG)

    def ShowTaskInfo(self):
        print(f"{self.name:30} {"Yes" if self.checked else "No":20} {str(self.creationTime):30} {enums.TaskPriority(self.priority).name:20} {self.tags}")

    def GetName(self): return self.name
    def GetChecked(self): return self.checked
    def GetCreationDate(self): return self.creationTime
    def GetCheckedDate(self): return self.checkedDate
    def GetPriority(self): return self.priority
    def GetTags(self): return self.tags

    def SetName(self, name:str):
        self.name = name

    def SetCreationDate(self, date):
        self.creationTime = date

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

    def UpdateFields(self, name:str="", priority:int=enums.TaskPriority.NONE, tags:list=[], checked:bool=False):
        if (name != ""): self.SetName(name=name)
        if (priority != -1): self.SetPriority(priority=priority)
        if (len(tags) == 0): self.SetTags(tags=tags)
        if (checked) : self.CheckTask()

    def ConvertTagsToString(tags:list):
        tagString = str(tags)[1:len(str(tags))-1]
        tagString = tagString.replace("\'", "")
        tagString = tagString.replace(", ", ",")
        return tagString