import tasklist
import enums
import sql_db
import task as Task

class App:
    def __init__(self):
        self.CURRENT_MENU = enums.Menu.MAIN_MENU.value
        self.CURRENT_TASK_LIST = None
        self.TASKLIST = {}
        self._LoadData()

    def _LoadData(self):
        with sql_db.Database() as db:
            dbData = db.LoadTaskLists()
            if len(dbData) != 0: 
                for data in dbData:
                    self.TASKLIST[data['name']] = tasklist.TaskList(name=data['name'], 
                                                                    creationDate=data['creationDate'])
                    taskListID = data['id']
                    taskData = db.LoadTaskInTasklist(tasklistID=taskListID)
                    if len(dbData) != 0:
                        for task in taskData:
                            self.TASKLIST[data['name']].CreateTask(name=task['name'],
                                                                    checked=bool(task['checked']),
                                                                    priority=task['priority'],
                                                                    tags=task['tags'],
                                                                    creationDate=task['creationDate'])


    def ChangeMenu(self, menu):
        if (menu == enums.Menu.MAIN_MENU.value):
            self.CURRENT_MENU = enums.Menu.MAIN_MENU.value
            self.CURRENT_TASK_LIST = None
            print(f"{"-"*enums._LINE_STAR_COUNT}\nSwitching To Main Menu\n{"-"*enums._LINE_STAR_COUNT}")
        elif (menu not in self.TASKLIST):
            print(enums.PrintStatements.NO_TASK_LIST_EXIST.value)
            print(enums.PrintStatements.RETURNING_TO_MAIN_MENU.value)
            self.CURRENT_MENU = enums.Menu.MAIN_MENU.value
            self.CURRENT_TASK_LIST = None
        else:
            self.CURRENT_TASK_LIST = menu
            self.CURRENT_MENU = enums.Menu.IN_TASK_LIST.value
            print(f"{"-"*enums._LINE_STAR_COUNT}\nSwitching To {self.CURRENT_TASK_LIST}\n{"-"*enums._LINE_STAR_COUNT}")

    def ShowCurrentMenu_Text(self):
        if (self.CURRENT_MENU == enums.Menu.MAIN_MENU.value): return "Main Menu"
        if (self.CURRENT_MENU != enums.Menu.MAIN_MENU.value and self.CURRENT_TASK_LIST is not None): return self.CURRENT_TASK_LIST
        return "Unknown"

    def ShowCurrentMenu(self):
        print(f"You Are Currently In -> {self.ShowCurrentMenu_Text()}")

    def ViewTasksInList(self):
        self.TASKLIST.get(self.CURRENT_TASK_LIST).ShowTasks()

    def CreateTaskInList(self, name:str):
        if (name == ""):
            return -1
        checked = str(input("Checked ? : ")).lower().lstrip()
        priority = str(input("Priority ? : ")).lower().lstrip()
        tags = str(input("Tags ? : ")).lower().lstrip()
        self.TASKLIST.get(self.CURRENT_TASK_LIST).CreateTask(name=name, 
                                                             checked=checked, 
                                                             priority=priority, 
                                                             tags=tags)

    def DeleteTaskInList(self, index:int):
        self.TASKLIST.get(self.CURRENT_TASK_LIST).DeleteTask(index=index)

    def CheckUncheckTaskInList(self, index:int, checked:bool=False):
        self.TASKLIST.get(self.CURRENT_TASK_LIST).CheckUncheckTask(index=index, 
                                                                   checked=checked)
            
    def CreateTaskList(self, name:str = ""):
        name = name.lstrip()
        if (name == ""):
            name = str(input("Enter The Name For Task List : "))
        if (name in self.TASKLIST):
            print("ERROR")
            return -1
        newTaskList = tasklist.TaskList(name=name)
        self.TASKLIST[name] = newTaskList
        print(enums.PrintStatements.NEW_TASK_LIST_CREATED.value)

    def DeleteTaskList(self, name:str = ""):
        name = name.lstrip()
        if (name == ""):
            name = str(input("Enter The Name For Task List : "))
        if (name not in self.TASKLIST):
            print("ERROR")
            return -1
        del self.TASKLIST[name]
        print(enums.PrintStatements.TASK_LIST_DELETED.value)

    def UpdateTaskList(self, name:str = "", newName:str = ""):
        name = name.lstrip()
        if (name == ""):
            name = str(input("Enter The Name For Task List : "))
        if (newName == ""):
            newName = str(input("Enter The New Name For Task List : "))
        if (name not in self.TASKLIST or newName in self.TASKLIST):
            print("ERROR")
            return -1
        task = self.TASKLIST.pop(name)
        task.UpdateName(newName)
        self.TASKLIST[newName] = task
        print(enums.PrintStatements.TASK_LIST_UPDATED.value)

    def GetAllTaskLists(self):
        if (len(self.TASKLIST) < 1): print(enums.PrintStatements.NO_TASK_LIST_EXIST.value)
        else:
            tasks = list(self.TASKLIST.values())
            tasks[0].ShowTaskListInfo_Header()
            for i in range(len(tasks)):
                print(f"{i:3} {" ":10} ", end="")
                tasks[i].ShowTaskListInfo()
        print("-"*enums._LINE_STAR_COUNT_BIG)
                

    def PrintExitStatement(self):
        print(enums.PrintStatements.EXIT_STATEMENT.value)

    def PrintHelp(self, menu:str=enums.Menu.MAIN_MENU.value):
        match menu:
            case enums.Menu.IN_TASK_LIST.value:
                print(enums.PrintStatements.IN_TASK_LIST_HELP.value)
            # case enums.Menu.IN_TASK.value:
            #     print("...")
            case _:
                print(enums.PrintStatements.MAIN_MENU_HELP.value)

    def SaveData(self):
        with sql_db.Database() as db:
            db.DropAllTables(makeNewTable=True)
            for tasklist in self.TASKLIST.values():
                tasklistID = db.CreateTaskList(name=tasklist.GetName(), 
                                               creationDate=tasklist.GetCreationDate())
                tasks = tasklist.GetTasks()
                if (tasks is not None):
                    for task in tasks:
                        db.CreateTask(tasklistID=tasklistID,
                                        name=task.GetName(),
                                        checked=int(task.GetChecked()), 
                                        creationDate=str(task.GetCreationDate()), 
                                        priority=int(task.GetPriority()), 
                                        tags=Task.Task.ConvertTagsToString(tags=task.GetTags()))
        print(enums.PrintStatements.SAVED_SUCCESSFULLY.value)

    def ArgParse(self, userInput:str):
        if (userInput[0] == ""): return 0
        if (userInput[0] in enums.Args.HELP.value): self.PrintHelp(menu=self.CURRENT_MENU); return 0
        if (userInput[0] in enums.Args.MAIN.value): self.ChangeMenu(menu=enums.Menu.MAIN_MENU.value); return 0
        if (userInput[0] in enums.Args.EXIT.value): self.PrintExitStatement(); return 1
        if (userInput[0] in enums.Args.SAVE.value): self.SaveData(); return 0
        if (userInput[0] in enums.Args.CLEAR.value): return 0

        if (self.CURRENT_MENU == enums.Menu.MAIN_MENU.value):
            if (userInput[0] in enums.Args.LISTS.value): self.GetAllTaskLists(); return 0
            if (userInput[0] in enums.Args.CREATE.value): self.CreateTaskList("" if len(userInput) < 2 else userInput[1]); return 0
            if (userInput[0] in enums.Args.DELETE.value): self.DeleteTaskList("" if len(userInput) < 2 else userInput[1]); return 0
            if (userInput[0] in enums.Args.OPEN.value): self.ChangeMenu("" if len(userInput) < 2 else userInput[1]); return 0
            print("Invalid State")
        elif (self.CURRENT_MENU == enums.Menu.IN_TASK_LIST.value and self.CURRENT_TASK_LIST in self.TASKLIST):
            if (userInput[0] in enums.Args.VIEW.value): self.ViewTasksInList(); return 0
            if (userInput[0] in enums.Args.CREATE.value): self.CreateTaskInList(name="" if len(userInput) < 2 else userInput[1]); return 0
            if (userInput[0] in enums.Args.UPDATE.value): pass; return 0
            if (userInput[0] in enums.Args.DELETE.value): self.DeleteTaskInList(index=0 if len(userInput) < 2 else int(userInput[1])); return 0
            if (userInput[0] in enums.Args.CHECK.value): self.CheckUncheckTaskInList(index=0 if len(userInput) < 2 else int(userInput[1]), checked=True); return 0
            if (userInput[0] in enums.Args.UNCHECK.value): self.CheckUncheckTaskInList(index=0 if len(userInput) < 2 else int(userInput[1]), checked=False); return 0
        else:
            print("Invalid State")
            print(self.TASKLIST)
            print(self.CURRENT_MENU)
            return -1