import sys
import datetime
import webbrowser
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QCheckBox, QDialog, QLineEdit, QMessageBox)
from PyQt6.QtGui import QGuiApplication, QColor, QIcon
from PyQt6.QtCore import QSize, Qt
import enums

SPLIT = 30

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._windowWidth = 1200
        self._windowHeight = 700

        # Main Window Parameters
        self.setWindowTitle(enums.APPNAME)
        self.setGeometry(int((QGuiApplication.primaryScreen().geometry().width() - self._windowWidth) // 2), 
                         int((QGuiApplication.primaryScreen().geometry().height() - self._windowHeight) // 2), 
                         self._windowWidth,
                         self._windowHeight)
        self.setMinimumSize(self._windowWidth, self._windowHeight)

        # Starts Setting Up UI
        self.InitUI()
        self.InitStyleSheets()
    
    def InitUI(self) -> None:
        self._centalWidget = QWidget()
        self._centalWidget.setObjectName("centralWidget")
        self.setCentralWidget(self._centalWidget)

        mainHLayout = QHBoxLayout()
        sideBarVLayout = QVBoxLayout()
        
        sideBarVLayout.addWidget(self.CreateSidebarTitleCard())
        sideBarVLayout.addWidget(self.CreateSideBarScroller())

        mainTaskLayout = QVBoxLayout()
        mainTaskLayout.addWidget(self.CreateMainbarTitleCard())
        mainTaskLayout.addWidget(self.CreateMainSideScroller())

        mainHLayout.addLayout(sideBarVLayout, SPLIT)
        mainHLayout.addLayout(mainTaskLayout, 100-SPLIT)
        self._centalWidget.setLayout(mainHLayout)

    def CreateSidebarTitleCard(self):
        mainWidget = QWidget()
        mainHLayout = QHBoxLayout()
        mainHLayout.addWidget(self.CreateTitleWidget())
        mainHLayout.addStretch()
        mainHLayout.addWidget(self.CreateSideBarTitleCard_AddTaskListButton())
        mainWidget.setLayout(mainHLayout)
        return mainWidget

    def CreateMainbarTitleCard(self):
        mainWidget = QWidget()
        mainHLayout = QHBoxLayout()
        mainHLayout.addWidget(self.CreateSubTitleWidget())
        mainHLayout.addStretch()
        mainHLayout.addWidget(self.CreateMainBarTitleCard_DeleteTaskListButton())
        mainHLayout.addWidget(self.CreateMainBarTitleCard_AddTaskButton())
        mainWidget.setLayout(mainHLayout)
        return mainWidget

    def CreateSideBarTitleCard_AddTaskListButton(self):
        mainButton = QPushButton("+")
        mainButton.setObjectName("AddTaskListButton")
        mainButton.clicked.connect(self.CreateTaskInfoCreationDialog)
        return mainButton

    def CreateMainBarTitleCard_AddTaskButton(self):
        mainButton = QPushButton("+")
        mainButton.setObjectName("AddTaskButton")
        mainButton.clicked.connect(self.CreateTaskDialog)
        return mainButton
    
    def CreateMainBarTitleCard_DeleteTaskListButton(self):
        mainButton = QPushButton("-")
        mainButton.setObjectName("DeleteTaskListButton")
        mainButton.clicked.connect(self.ShowWarningDialog)
        return mainButton

    def CreateTitleWidget(self):
        titleLabel = QLabel(enums.APPNAME, self)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        titleLabel.setStyleSheet("""
            font-size: 52px;
            font-family: "Rubik";
            font-weight: 600;
            margin: 15px 0px 15px 0px;
        """)
        return titleLabel

    def CreateSubTitleWidget(self):
        titleLabel = QLabel("Task List Name", self)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
        titleLabel.setStyleSheet("""
            font-size: 32px;
            font-family: "Rubik";
            font-weight: 600;
            margin: 33px 0px 33px 0px;
        """)
        return titleLabel

    def CreateSideBarScroller(self):
        scrollWidget = QScrollArea()
        scrollWidget.setWidgetResizable(True)
        scrollAreaContainer = QWidget()
        scrollArea= QVBoxLayout(scrollAreaContainer)
        scrollArea.addWidget(self.CreateTaskListButton_Header())
        for x in range(100):
            scrollArea.addWidget(self.CreateTaskListButton(f"Hello{x}", x))

        scrollWidget.setWidget(scrollAreaContainer)
        return scrollWidget

    def CreateMainSideScroller(self):
        scrollWidget = QScrollArea()
        scrollWidget.setWidgetResizable(True)
        scrollAreaContainer = QWidget()
        scrollArea = QVBoxLayout(scrollAreaContainer)
        scrollArea.addWidget(self.CreateTaskButton_Header())
        for x in range(100):
            scrollArea.addWidget(self.CreateTaskButton())

        scrollWidget.setWidget(scrollAreaContainer)
        return scrollWidget

    def CreateTaskListButton_Header(self):
        mainWidget = QWidget()
        mainHLayout = QHBoxLayout()
        title = QLabel("List Name", self)
        totalTasks = QLabel("Total Tasks", self)
        openButton = QLabel("Open Button", self)

        title.setObjectName("sideBarHeaderTitle")
        totalTasks.setObjectName("sideBarHeaderTitle")
        openButton.setObjectName("sideBarHeaderTitle")

        mainHLayout.addWidget(title)
        mainHLayout.addStretch()
        mainHLayout.addWidget(totalTasks)
        mainHLayout.addStretch()
        mainHLayout.addWidget(openButton)
        mainWidget.setLayout(mainHLayout)

        return mainWidget

    def CreateTaskListButton(self, name:str, taskLen:int):
        mainWidget = QWidget()
        mainWidget.setObjectName("TaskEntry")
        mainHLayout = QHBoxLayout()
        title = QLabel(name, self)
        totalTasks = QLabel(str(taskLen), self)
        openButton = QPushButton(">>", self)
        openButton.setObjectName("TaskListEntryButton")

        mainHLayout.addWidget(title)
        mainHLayout.addStretch()
        mainHLayout.addWidget(totalTasks)
        mainHLayout.addStretch()
        mainHLayout.addWidget(openButton)
        mainWidget.setLayout(mainHLayout)

        return mainWidget

    def CreateTaskButton_Header(self):
        mainWidget = QWidget()
        mainHLayout = QHBoxLayout()
        checkBox = QLabel("Task Name", self)
        priority = QLabel("Priority", self)
        date = QLabel("Creation Date", self)
        delButton = QLabel("Delete", self)
        openButton = QLabel("Details", self)

        checkBox.setObjectName("mainBarHeaderTitle")
        priority.setObjectName("mainBarHeaderTitle")
        openButton.setObjectName("mainBarHeaderTitle")
        date.setObjectName("mainBarHeaderTitle")
        delButton.setObjectName("mainBarHeaderTitle")

        mainHLayout.addWidget(checkBox)
        mainHLayout.addStretch()
        mainHLayout.addWidget(priority)
        mainHLayout.addStretch()
        mainHLayout.addWidget(date)
        mainHLayout.addStretch()
        mainHLayout.addWidget(delButton)
        mainHLayout.addWidget(openButton)
        mainWidget.setLayout(mainHLayout)

        return mainWidget

    def CreateTaskButton(self):
        mainWidget = QWidget()
        mainWidget.setObjectName("TaskEntry")
        mainHLayout = QHBoxLayout()
        checkBox = QCheckBox("Task Name", self)
        priority = QLabel("NONE", self)
        date = QLabel("26 Jan, 2007", self)
        openButton = QPushButton(">>", self)
        delButton = QPushButton("D", self)
        openButton.setObjectName("TaskListEntryButton")
        openButton.clicked.connect(self.CreateTaskInfoDialog)
        delButton.setObjectName("TaskDeleteButton")
        delButton.clicked.connect(self.ShowWarningDialog)

        mainHLayout.addWidget(checkBox)
        mainHLayout.addStretch()
        mainHLayout.addWidget(priority)
        mainHLayout.addStretch()
        mainHLayout.addWidget(date)
        mainHLayout.addStretch()
        mainHLayout.addWidget(delButton)
        mainHLayout.addWidget(openButton)
        mainWidget.setLayout(mainHLayout)

        return mainWidget

    def CreateTaskInfoDialog(self):
        dialog = TaskInfoDialog()
        dialog.exec()

    def CreateTaskDialog(self):
        dialog = CreateTaskDialog()
        dialog.exec()

    def CreateTaskInfoCreationDialog(self):
        dialog = CreateTaskListDialog()
        dialog.exec()

    def ShowWarningDialog(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Warning!")
        dlg.setText("WAAA")
        dlg.setIcon(QMessageBox.Icon.Warning)
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        button = dlg.exec()
        if button == QMessageBox.StandardButton.Yes:
            print("Yes!")
        else:
            print("No!")

    def InitStyleSheets(self) -> None:
        self.setStyleSheet(enums.PyQt6StyleSheet.STYLESHEET.value)

    def UpdateUI(self) -> None:
        self.InitUI()

class CreateTaskListDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Task List")

        self._windowWidth = 600
        self._windowHeight = 200

        self.setGeometry(int((QGuiApplication.primaryScreen().geometry().width() - self._windowWidth) // 2), 
                         int((QGuiApplication.primaryScreen().geometry().height() - self._windowHeight) // 2), 
                         self._windowWidth,
                         self._windowHeight)
        
        self.setMinimumSize(self._windowWidth, self._windowHeight)
        self.setMaximumSize(self._windowWidth, self._windowHeight)

        self.InitUI()
        self.InitStyleSheets()

    def InitUI(self):
        mainWindowLayout = QVBoxLayout()

        name = QLabel("Create New Task List", self)
        name.setObjectName("TitleCardObject")
        mainWindowLayout.addStretch()
        mainWindowLayout.addWidget(name)
        mainWindowLayout.addStretch()
        mainWindowLayout.addWidget(self.CreateInputFieldOption(name="Name"))
        mainWindowLayout.addStretch()

        saveButton = QPushButton("Create", self)
        saveButton.setObjectName("SaveButtonWidget")
        mainWindowLayout.addWidget(saveButton)

        self.setLayout(mainWindowLayout)

    def CreateInputFieldOption(self, name:str):
        mainContainer = QWidget()
        mainLayout = QHBoxLayout()

        field = QLabel(name, self)
        field.setObjectName("FieldNameTitle")
        fieldInput = QLineEdit(self)
        mainLayout.addWidget(field)
        mainLayout.addWidget(fieldInput)

        mainContainer.setLayout(mainLayout)
        return mainContainer

    def InitStyleSheets(self):
        self.setStyleSheet(enums.PyQt6StyleSheet.STYLESHEET.value)

class TaskInfoDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Information")

        self._windowWidth = 600
        self._windowHeight = 400

        self.setGeometry(int((QGuiApplication.primaryScreen().geometry().width() - self._windowWidth) // 2), 
                         int((QGuiApplication.primaryScreen().geometry().height() - self._windowHeight) // 2), 
                         self._windowWidth,
                         self._windowHeight)
        
        self.setMinimumSize(self._windowWidth, self._windowHeight)
        self.setMaximumSize(self._windowWidth, self._windowHeight)

        self.InitUI()
        self.InitStyleSheets()

    def InitUI(self):
        mainWindowLayout = QVBoxLayout()
        data = ['Name', 'Priority', 'Tags', 'Creation Date', 'Checked Date']

        titleCard = QLabel("Task Information", self)
        titleCard.setObjectName("TitleCardObject")
        mainWindowLayout.addStretch()
        mainWindowLayout.addWidget(titleCard)
        mainWindowLayout.addStretch()

        for name in data:
            mainWindowLayout.addWidget(self.CreateInputFieldOption(name=name, editable=False if name in ('Creation Date', 'Checked Date') else True))

        mainWindowLayout.addStretch()

        saveButton = QPushButton("Save Changes", self)
        saveButton.setObjectName("SaveButtonWidget")
        mainWindowLayout.addWidget(saveButton)

        self.setLayout(mainWindowLayout)

    def CreateInputFieldOption(self, name:str, editable:bool):
        mainContainer = QWidget()
        mainLayout = QHBoxLayout()

        field = QLabel(f"{name}", self)
        field.setObjectName("FieldNameTitle")
        if (editable): 
            fieldInput = QLineEdit(self)
        else: 
            fieldInput = QLabel("Whatever", self)

        mainLayout.addWidget(field)
        mainLayout.addStretch()
        mainLayout.addWidget(fieldInput)

        mainContainer.setLayout(mainLayout)
        return mainContainer


    def InitStyleSheets(self):
        self.setStyleSheet(enums.PyQt6StyleSheet.STYLESHEET.value)

class CreateTaskDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create Task")

        self._windowWidth = 600
        self._windowHeight = 300

        self.setGeometry(int((QGuiApplication.primaryScreen().geometry().width() - self._windowWidth) // 2), 
                         int((QGuiApplication.primaryScreen().geometry().height() - self._windowHeight) // 2), 
                         self._windowWidth,
                         self._windowHeight)
        
        self.setMinimumSize(self._windowWidth, self._windowHeight)
        self.setMaximumSize(self._windowWidth, self._windowHeight)

        self.InitUI()
        self.InitStyleSheets()

    def InitUI(self):
        mainWindowLayout = QVBoxLayout()
        data = ['Name', 'Priority', 'Tags']

        titleCard = QLabel("Create Task", self)
        titleCard.setObjectName("TitleCardObject")
        mainWindowLayout.addStretch()
        mainWindowLayout.addWidget(titleCard)
        mainWindowLayout.addStretch()

        for name in data:
            mainWindowLayout.addWidget(self.CreateInputFieldOption(name=name))

        mainWindowLayout.addStretch()

        saveButton = QPushButton("Create", self)
        saveButton.setObjectName("SaveButtonWidget")
        mainWindowLayout.addWidget(saveButton)

        self.setLayout(mainWindowLayout)

    def CreateInputFieldOption(self, name:str):
        mainContainer = QWidget()
        mainLayout = QHBoxLayout()

        field = QLabel(f"{name}", self)
        field.setObjectName("FieldNameTitle")
        fieldInput = QLineEdit(self)

        mainLayout.addWidget(field)
        mainLayout.addStretch()
        mainLayout.addWidget(fieldInput)

        mainContainer.setLayout(mainLayout)
        return mainContainer


    def InitStyleSheets(self):
        self.setStyleSheet(enums.PyQt6StyleSheet.STYLESHEET.value)

def MainLoop():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())