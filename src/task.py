# Imports
import datetime
import enums

# Class to create a new task.
class Task:

    # Initializer for the class.
    # Creates a task.
    def __init__(self, name:str, checked:bool, creationTime=datetime.datetime.now(), priority:int=enums.TaskPriority.NONE, tags:list=[]):
        self.name = name
        self.checked = checked
        self.creationTime = creationTime
        self.checkedDate = ""
        self.priority = priority
        self.tags = tags

    # ---------------------------------------

    # Prints the header for the task information, object independent.
    def ShowTaskInfo_Header(cls):
        print("-"*enums._LINE_STAR_COUNT_BIG)
        print(f"{"UID":3} {" ":10} {"Task Name":30} {"Checked":20} {"Creation Date":30} {"Priority":20} Tags")
        print("-"*enums._LINE_STAR_COUNT_BIG)

    # ---------------------------------------

    # Prints the task information.
    def ShowTaskInfo(self):
        print(f"{self.name:30} {"Yes" if self.checked else "No":20} {str(self.creationTime):30} {enums.TaskPriority(self.priority).name:20} {self.tags}")

    # ---------------------------------------

    # Generic functions to return attribute names.
    def GetName(self): return self.name
    def GetChecked(self): return self.checked
    def GetCreationDate(self): return self.creationTime
    def GetCheckedDate(self): return self.checkedDate
    def GetPriority(self): return self.priority
    def GetTags(self): return self.tags

    # ---------------------------------------

    # Generic functions to set attribute values.
    def SetName(self, name:str): self.name = name
    def SetCreationDate(self, date): self.creationTime = date
    def SetPriority(self, priority:int=enums.TaskPriority.NONE): self.priority = priority
    def SetTags(self, tags:list=[]): self.tags.extend(tags)

    # ---------------------------------------

    # Generic functions to set check or uncheck a task.
    def CheckTask(self):
        self.checked = True
        self.checkedDate = datetime.datetime.now()

    def UnCheckTask(self):
        self.checked = False
        self.checkedDate = ""

    # ---------------------------------------

    # Function meant to update a task.
    # Allows for flexibility of fields.
    def UpdateFields(self, name:str="", priority:int=enums.TaskPriority.NONE, tags:list=[], checked:bool=False):
        if (name != ""): self.SetName(name=name)
        if (priority != -1): self.SetPriority(priority=priority)
        if (len(tags) != 0): self.SetTags(tags=tags)
        if (checked) : self.CheckTask()

    # ---------------------------------------

    # Converts the tags list into a string of proper formatting.
    # Object independent.
    def ConvertTagsToString(tags:list):
        tagString = str(tags)[1:len(str(tags))-1]
        tagString = tagString.replace("\'", "")
        tagString = tagString.replace(", ", ",")
        return tagString