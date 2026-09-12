import task
import tasklist
import enums

class App:
    def __init__(self):
        self.CURRENT_MENU = enums.Menu.MAIN_MENU.value
        self.CURRENT_TASK_LIST = None
        self.TASKLIST = {}

    def ChangeMenu(self, menu):
        if (menu == enums.Menu.MAIN_MENU):
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

    def ViewTasksInList(self):
        self.TASKLIST.get(self.CURRENT_TASK_LIST).ShowTasks()

    def CreateTaskInList(self, name:str):
        if (name == ""):
            return -1
        checked = str(input("Checked ? : ")).lower().lstrip()
        priority = str(input("Priority ? : ")).lower().lstrip()
        tags = str(input("Tags ? : ")).lower().lstrip()
        self.TASKLIST.get(self.CURRENT_TASK_LIST).CreateTask(name=name, checked=checked, priority=priority, tags=tags)

    def DeleteTaskInList(self, index:int):
        self.TASKLIST.get(self.CURRENT_TASK_LIST).DeleteTask(index=index)

    def CheckUncheckTaskInList(self, index:int, checked:bool=False):
        self.TASKLIST.get(self.CURRENT_TASK_LIST).CheckUncheckTask(index=index, checked=checked)
            
    def CreateTaskList(self, name:str = ""):
        if (name == ""):
            name = str(input("Enter The Name For Task List : "))
        if (name in self.TASKLIST):
            print("ERROR")
            return -1
        newTaskList = tasklist.TaskList(name=name)
        self.TASKLIST[name] = newTaskList

    def DeleteTaskList(self, name:str = ""): 
        if (name == ""):
            name = str(input("Enter The Name For Task List : "))
        if (name in self.TASKLIST):
            print("ERROR")
            return -1
        del self.TASKLIST[name]

    def GetAllTaskLists(self):
        if (len(self.TASKLIST) < 1): print(enums.PrintStatements.NO_TASK_LIST_EXIST.value)
        else:
            for tasklist in self.TASKLIST.values():
                print(tasklist.GetName()) # TODO: DO LATER

    def PrintExitStatement(self):
        print(enums.PrintStatements.EXIT_STATEMENT.value)

    def PrintHelp(self, menu:str=enums.Menu.MAIN_MENU.value):
        match menu:
            case enums.Menu.IN_TASK_LIST.value:
                print("...")
            case enums.Menu.IN_TASK.value:
                print("...")
            case _:
                print(enums.PrintStatements.MAIN_MENU_HELP.value)

    def ArgParse(self, userInput:str):
        if (userInput[0] in enums.Args.HELP.value): self.PrintHelp(menu=self.CURRENT_MENU); return 0
        if (userInput[0] in enums.Args.MAIN.value): self.ChangeMenu(menu=enums.Menu.MAIN_MENU.value); return 0
        if (userInput[0] in enums.Args.EXIT.value): self.PrintExitStatement(); return 1

        if (self.CURRENT_MENU == enums.Menu.MAIN_MENU.value):
            if (userInput[0] in enums.Args.LISTS.value): self.GetAllTaskLists(); return 0
            if (userInput[0] in enums.Args.CREATE.value): self.CreateTaskList("" if len(userInput) < 2 else userInput[1]); return 0
            if (userInput[0] in enums.Args.DELETE.value): self.DeleteTaskList("" if len(userInput) < 2 else userInput[1]); return 0
            if (userInput[0] in enums.Args.OPEN.value): self.ChangeMenu("" if len(userInput) < 2 else userInput[1]); return 0
            print("Invalid State")
        elif (self.CURRENT_MENU == enums.Menu.IN_TASK_LIST.value and self.CURRENT_TASK_LIST in self.TASKLIST):
            if (userInput[0] in enums.Args.OPEN.value): self.ViewTasksInList(); return 0
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