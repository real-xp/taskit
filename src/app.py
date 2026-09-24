# Import Statements
import tasklist
import enums
import sql_db
import task as Task

# Actual class for the App working
class App:

    # Initializer for the class.
    # Creates an empty tasklist.
    # Creates varaibles for current menu, and current task list opened.
    # Loads data from DB if exists.
    def __init__(self):
        self.CURRENT_MENU = enums.Menu.MAIN_MENU.value
        self.CURRENT_TASK_LIST = None
        self.TASKLIST = {}
        self._LoadData()

    # ---------------------------------------

    # Loads the data from the SQLite database db file if it exiss, and if not, it creates a db file.
    # It first iterates over the list of tasks, and per task list, it then iterates over the tasks and puts them in the tasks.
    # Based on Unique incremental keys for IDs
    def _LoadData(self) -> None:
        with sql_db.Database() as db: # Safe Resource Loading
            dbData = db.LoadTaskLists()
            if len(dbData) != 0: 
                for data in dbData:
                    self.TASKLIST[data['name']] = tasklist.TaskList(name=data['name'], 
                                                                    creationDate=data['creationDate'])
                    taskListID = data['id']
                    taskData = db.LoadTaskInTasklist(tasklistID=taskListID)

                    if len(taskData) != 0:
                        for task in taskData:
                            self.TASKLIST[data['name']].CreateTask(name=task['name'],
                                                                    checked=bool(task['checked']),
                                                                    priority=task['priority'],
                                                                    tags=task['tags'],
                                                                    creationDate=task['creationDate'])

    # ---------------------------------------

    # This function is used for saving the entire data from the memory onto the SQLite database.
    # What it essentially does is it drops all previously made tables, and remakes them.
    # This is done so to avoid checking and updating and deleting each and every entry separately using queries.
    # This saves time, but can be heavy on memory usage / cpu usage for a brief second with large datasets.
    # If all is successful, it prints a success message.
    def SaveData(self) -> None:
        rqCode = 0
        with sql_db.Database() as db:

            rqCode = db.DropAllTables(makeNewTable=True) # Deletes all tables currently to remake the database

            if rqCode != 0:
                return

            for tasklist in self.TASKLIST.values():
                tasklistID = db.CreateTaskList(name=tasklist.GetName(), 
                                               creationDate=tasklist.GetCreationDate())
                tasks = tasklist.GetTasks() # Gets all the tasks in a particular tasklist

                if (tasks != []):
                    for task in tasks:
                        db.CreateTask(tasklistID=tasklistID,
                                        name=task.GetName(),
                                        checked=int(task.GetChecked()), 
                                        creationDate=str(task.GetCreationDate()), 
                                        priority=int(task.GetPriority()), 
                                        tags=Task.Task.ConvertTagsToString(tags=task.GetTags()))

        if rqCode == 0:
            print(enums.PrintStatements.SAVED_SUCCESSFULLY.value)

    # ---------------------------------------

    # This function is used for changing the menu the user is currently in.
    # It can change between either the Main Menu, or a proper task list as its menu.
    # If a menu is invalid, it switches back to Main Menu.
    def ChangeMenu(self, menu) -> None:
        if menu is str:
            menu = menu.strip()

        if (menu == enums.Menu.MAIN_MENU.value):
            self.CURRENT_MENU = enums.Menu.MAIN_MENU.value
            self.CURRENT_TASK_LIST = None

            print(f"{"-"*enums._LINE_STAR_COUNT}\nSwitching To Main Menu\n{"-"*enums._LINE_STAR_COUNT}")

        elif (menu not in self.TASKLIST):
            self.CURRENT_MENU = enums.Menu.MAIN_MENU.value
            self.CURRENT_TASK_LIST = None

            print(enums.PrintStatements.NO_TASK_LIST_EXIST.value)
            print(enums.PrintStatements.RETURNING_TO_MAIN_MENU.value)

        else:
            self.CURRENT_TASK_LIST = menu
            self.CURRENT_MENU = enums.Menu.IN_TASK_LIST.value

            print(f"{"-"*enums._LINE_STAR_COUNT}\nSwitching To {self.CURRENT_TASK_LIST}\n{"-"*enums._LINE_STAR_COUNT}")

    # ---------------------------------------

    # This function shows what menu you are currently in.
    # If you are in the Main Menu, it shows that.
    # If you are in a tasklist, it shows that.
    # Otherwise, it is Unknown.
    def ShowCurrentMenu_Text(self) -> str:
        if (self.CURRENT_MENU == enums.Menu.MAIN_MENU.value): return "Main Menu"
        if (self.CURRENT_MENU != enums.Menu.MAIN_MENU.value and self.CURRENT_TASK_LIST is not None): return self.CURRENT_TASK_LIST
        return "Unknown"

    # ---------------------------------------

    # This is the main menu showing function
    def ShowCurrentMenu(self) -> None:
        print(f"You Are Currently In -> {self.ShowCurrentMenu_Text()}")

    # ---------------------------------------

    # Retrieves all the tasks in a tasklist.
    def ViewTasksInList(self) -> None:
        self.TASKLIST.get(self.CURRENT_TASK_LIST).ShowTasks()

    # ---------------------------------------

    # This function creates a new task inside the defined tasklist.
    # It asks for priority, checked status, tags and then commits it.
    def CreateTaskInList(self, name:str) -> None:
        if (name.strip() == ""):
            name = str(input("Enter The Name For Task : ")).strip()
        
        checked = str(input("Checked ? : ")).lower().strip()
        priority = str(input("Priority ? : ")).lower().strip()
        tags = str(input("Tags ? : ")).lower().strip()

        self.TASKLIST.get(self.CURRENT_TASK_LIST).CreateTask(name=name.strip(), 
                                                             checked=checked, 
                                                             priority=priority, 
                                                             tags=tags)

        print(enums.PrintStatements.TASK_CREATED.value)

    # ---------------------------------------

    # Deletes the task at that index.
    def DeleteTaskInList(self, index:str) -> None:
        if index == "":
            index = str(input("Enter the index for the task : ")).strip()
        try:
            index = int(index)
            self.TASKLIST.get(self.CURRENT_TASK_LIST).DeleteTask(index=index)
        except ValueError:
            print(enums.PrintStatements.NO_TASK_FOUND.value)

    # ---------------------------------------

    # Updates the task of a particular index.
    def UpdateTaskInList(self, index:str) -> None:
        if index == "":
            index = str(input("Enter the index for the task : ")).strip()
        try:
            index = int(index)
            name = str(input("Enter The Name For Task : ")).strip()
            checked = str(input("Checked ? : ")).lower().strip()
            priority = str(input("Priority ? : ")).lower().strip()
            tags = str(input("Tags ? : ")).lower().strip()

            if checked in enums.YesNo.YES.value:
                checked = True
            elif checked in enums.YesNo.NO.value:
                checked = False
            else:
                checked = None
            
            self.TASKLIST.get(self.CURRENT_TASK_LIST).UpdateTask(index=index, 
                                                                 name=name, 
                                                                 priority=priority, 
                                                                 tags=tags, 
                                                                 checked=checked)

        except ValueError:
            print(enums.PrintStatements.NO_TASK_FOUND.value)

    # ---------------------------------------

    # Function that can be used to check or uncheck a task in a tasklist.
    def CheckUncheckTaskInList(self, index:str, checked:bool=False) -> None:
        if index == "":
            index = str(input("Enter the index for the task : "))
        try:
            index = int(index)
            self.TASKLIST.get(self.CURRENT_TASK_LIST).CheckUncheckTask(index=index, checked=checked)
        except ValueError:
            print(enums.PrintStatements.NO_TASK_FOUND.value)

    # ---------------------------------------

    # Creates A Tasklist
    # If a name is not predefined, it asks for a name, else it continues.
    def CreateTaskList(self, name:str = "") -> None:
        name = name.strip()
        if (name == ""):
            name = str(input("Enter The Name For Task List : ")).strip()

        if (name in self.TASKLIST):
            print(enums.PrintStatements.TASK_LIST_ALREADY_EXISTS.value)
            return

        # Updates the task list name.
        newTaskList = tasklist.TaskList(name=name)
        self.TASKLIST[name] = newTaskList

        print(enums.PrintStatements.NEW_TASK_LIST_CREATED.value)

    # ---------------------------------------

    # Deletes A Tasklist
    # If a name is not predefined, it asks for a name, else it continues.
    # If a list does not exist, it throws an error.
    def DeleteTaskList(self, name:str = "") -> None:
        name = name.strip()
        if (name == ""):
            name = str(input("Enter The Name For Task List : ")).strip()

        if (name not in self.TASKLIST):
            print(enums.PrintStatements.NO_TASK_LIST_EXIST_SIMPLE.value)
            return
        
        del self.TASKLIST[name] # actual deletion of a tasklist.

        print(enums.PrintStatements.TASK_LIST_DELETED.value)
        self.ChangeMenu(menu=enums.Menu.MAIN_MENU.value)

    # ---------------------------------------

    # Updates A Tasklist
    # If a name is not predefined, it asks for a name, else it continues.
    # If a new name is not predefined, it asks for a new name, else it continues.
    def UpdateTaskList(self, name:str = "", newName:str = "") -> None:
        name = name.strip()
        if (name == ""):
            name = str(input("Enter The Name For Task List : ")).strip()

        if (name not in self.TASKLIST):
            print(enums.PrintStatements.NO_TASK_LIST_EXIST_SIMPLE.value)
            return

        if (newName == ""):
            newName = str(input("Enter The New Name For Task List : ")).strip()

        if (newName in self.TASKLIST):
            print(enums.PrintStatements.TASK_LIST_ALREADY_EXISTS_OTHER.value)
            return

        # This section basically removes the item from the dictionary, and then renames the task, and puts it back under a new key name
        if (name == "" or newName == ""):
            print(enums.PrintStatements.NO_TASK_LIST_EXIST_SIMPLE.value)
            return
        
        task = self.TASKLIST.pop(name)
        task.UpdateName(newName)
        self.TASKLIST[newName] = task

        print(enums.PrintStatements.TASK_LIST_UPDATED.value)

    # ---------------------------------------

    # Prints / Retrieves all tasks in a tasklist.
    # If a list has no tasks, it prints an error.
    # Else it will print it out in a tabular form.
    def GetAllTaskLists(self) -> None:
        if (len(self.TASKLIST) < 1): print(enums.PrintStatements.NO_TASK_LIST_EXIST.value)
        else:
            tasks = list(self.TASKLIST.values())
            tasks[0].ShowTaskListInfo_Header()

            for i in range(len(tasks)):
                print(f"{i:3} {" ":10} ", end="")
                tasks[i].ShowTaskListInfo()

        print("-"*enums._LINE_STAR_COUNT_BIG)
                
    # ---------------------------------------

    # Processes the exit statement and asks user if they want to save or not
    def ProcessExitStatement(self) -> int:
        askUser = str(input("Do you want to save before exiting? (Y/N) : ")).strip().lower()
        if (askUser in enums.YesNo.YES.value): 
            self.SaveData()
        print(enums.PrintStatements.EXIT_STATEMENT.value)
        return 0

    # ---------------------------------------

    # Function that prints help messages based on menu.
    # Modular, more menus can be added later.
    def PrintHelp(self, menu:str=enums.Menu.MAIN_MENU.value) -> None:
        match menu:
            case enums.Menu.IN_TASK_LIST.value:
                print(enums.PrintStatements.IN_TASK_LIST_HELP.value)
            case _:
                print(enums.PrintStatements.MAIN_MENU_HELP.value)

    # ---------------------------------------

    # Main function of this entire operation.
    # This function can shape time and reality itself.
    # It just sees if the user inputs are equal to what it asks for, and does appropriate actions based on that.
    # If not, it gives an error.
    def ArgParse(self, userInput:str) -> int:
        if (userInput[0] == ""): return 0
        if (userInput[0] in enums.Args.HELP.value): self.PrintHelp(menu=self.CURRENT_MENU); return 0
        if (userInput[0] in enums.Args.MAIN.value): self.ChangeMenu(menu=enums.Menu.MAIN_MENU.value); return 0
        if (userInput[0] in enums.Args.EXIT.value): self.ProcessExitStatement(); return 1
        if (userInput[0] in enums.Args.SAVE.value): self.SaveData(); return 0
        if (userInput[0] in enums.Args.CLEAR.value): return 0

        if (self.CURRENT_MENU == enums.Menu.MAIN_MENU.value):
            if (userInput[0] in enums.Args.LISTS.value): self.GetAllTaskLists(); return 0
            if (userInput[0] in enums.Args.CREATE.value): self.CreateTaskList(name="" if len(userInput) < 2 else userInput[1]); return 0
            if (userInput[0] in enums.Args.DELETE.value): self.DeleteTaskList(name="" if len(userInput) < 2 else userInput[1]); return 0
            if (userInput[0] in enums.Args.UPDATE.value): self.UpdateTaskList(name="" if len(userInput) < 2 else userInput[1], newName="" if len(userInput) < 3 else userInput[2]); return 0
            if (userInput[0] in enums.Args.OPEN.value): self.ChangeMenu("" if len(userInput) < 2 else userInput[1]); return 0
            print(enums.PrintStatements.INVALID_STATEMENT.value)
            return 0
            
        elif (self.CURRENT_MENU == enums.Menu.IN_TASK_LIST.value and self.CURRENT_TASK_LIST in self.TASKLIST):
            if (userInput[0] in enums.Args.VIEW.value): self.ViewTasksInList(); return 0
            if (userInput[0] in enums.Args.CREATE.value): self.CreateTaskInList(name="" if len(userInput) < 2 else userInput[1]); return 0
            if (userInput[0] in enums.Args.UPDATE.value): self.UpdateTaskInList(index="" if len(userInput) < 2 else userInput[1]); return 0; return 0
            if (userInput[0] in enums.Args.DELETE.value): self.DeleteTaskInList(index="" if len(userInput) < 2 else userInput[1]); return 0
            if (userInput[0] in enums.Args.CHECK.value): self.CheckUncheckTaskInList(index="" if len(userInput) < 2 else userInput[1], checked=True); return 0
            if (userInput[0] in enums.Args.UNCHECK.value): self.CheckUncheckTaskInList(index="" if len(userInput) < 2 else userInput[1], checked=False); return 0
            print(enums.PrintStatements.INVALID_STATEMENT.value)
            return 0
            
        else:
            print(enums.PrintStatements.MAJOR_ERROR_STATEMENT.value)
            return -1