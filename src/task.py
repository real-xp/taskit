# Imports
import datetime
import enums

# Class to create a new task.
class Task:

    # Initializer for the class.
    # Creates a task.
    def __init__(self, name:str, checked:bool, creationTime=None, priority:int=enums.TaskPriority.NONE, tags:list=None):
        self.name = name
        self.checked = checked
        self.creationTime = creationTime if creationTime is not None else datetime.datetime.now()
        self.checkedDate = ""
        self.priority = priority
        self.tags = tags if tags is not None else []

    # ---------------------------------------

    # Prints the header for the task information, object independent.
    def ShowTaskInfo_Header(cls) -> None:
        print("-"*enums._LINE_STAR_COUNT_BIG)
        print(f"{"UID":3} {" ":10} {"Task Name":30} {"Checked":20} {"Creation Date":30} {"Priority":20} Tags")
        print("-"*enums._LINE_STAR_COUNT_BIG)

    # ---------------------------------------

    # Prints the task information.
    def ShowTaskInfo(self) -> None:
        print(f"{self.name:30} {"Yes" if self.checked else "No":20} {str(self.creationTime):30} {enums.TaskPriority(self.priority).name:20} {self.tags}")

    # ---------------------------------------

    # Generic functions to return attribute names.
    def GetName(self) -> str: return self.name
    def GetChecked(self) -> bool: return self.checked
    def GetCreationDate(self): return self.creationTime
    def GetCheckedDate(self): return self.checkedDate
    def GetPriority(self) -> int: return self.priority
    def GetTags(self) -> list: return self.tags

    # ---------------------------------------

    # Generic functions to set attribute values.
    def SetName(self, name:str) -> None: self.name = name
    def SetCreationDate(self, date) -> None: self.creationTime = date
    def SetPriority(self, priority:int=enums.TaskPriority.NONE) -> None: self.priority = priority
    def SetTags(self, tags:list=None) -> None: 
        if tags is None: tags = []
        self.tags.extend(tags)

    # ---------------------------------------

    # Generic functions to set check or uncheck a task.
    def CheckTask(self) -> None:
        self.checked = True
        self.checkedDate = datetime.datetime.now()

    def UnCheckTask(self) -> None:
        self.checked = False
        self.checkedDate = ""

    # ---------------------------------------

    # Function meant to update a task.
    # Allows for flexibility of fields.
    def UpdateFields(self, name:str="", priority:int=enums.TaskPriority.NONE, tags:list=None, checked:bool=False) -> None:
        if tags is None: tags = []
        if (name != ""): self.SetName(name=name)
        if (priority != -1): self.SetPriority(priority=priority)
        if (len(tags) != 0): self.SetTags(tags=tags)
        if (checked) : self.CheckTask()

    # ---------------------------------------

    # Converts the tags list into a string of proper formatting.
    # Object independent.
    def ConvertTagsToString(tags:list) -> str:
        tagString = str(tags)[1:len(str(tags))-1]
        tagString = tagString.replace("\'", "")
        tagString = tagString.replace(", ", ",")
        return tagString