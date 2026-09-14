# Import Statements
import app as App
import getopt
import sys
import subprocess, platform
import webbrowser
import ui as AppUI

# CONSTANTS
WEB_PAGE_ONLINE = "https://github.com/real-xp/taskit/blob/main/README.md"

# This function's entire job is to clear the terminal based on the operating system for easier viewing.
def ClearTerminal() -> None:
    if (platform.system().lower() == 'windows'): subprocess.run('cls', shell=True)
    else: subprocess.run('clear', shell=True)

# ---------------------------------------

# Handles the cmd argument that one wants to throw at it
def ArgumentHandling():
    args = sys.argv[1:]

    if (len(args) == 0):
        return 0

    options = "hu"
    longOptions = ["help=", "ui="]
        
    try:
        arguments, values = getopt.getopt(args=args, shortopts=options, longopts=longOptions)
    except getopt.error as error:
        print(error)
        return -1

    for arg, val in arguments:
        if arg in ("-h", "--help"):
            webbrowser.open(WEB_PAGE_ONLINE)
            return -1
        
        elif arg in ("-u", "--ui"):
            return 1
            
# ---------------------------------------

# Main Program Loop
def main() -> int:
    UI = False
    result = ArgumentHandling()
    match result:
        case -1:
            return -1
        case 1:
            UI = True
        case _:
            pass

    if (not UI):
        
        app = App.App() # Init CMD Program
        app.PrintHelp() # Prints The Initial Help Message

        while (True):
            app.ShowCurrentMenu() # Prints the menu you are currently in
            userInput = [*map(str, str(input("What Operation Do You Want To Perform? : ")).lower().lstrip().split(";"))] # For User Input Mapping
            argResult = app.ArgParse(userInput=userInput) # Parses information from the user
            if (argResult in (1, -1)):
                break

            input("Press Any Key To Continue\n\n")
            ClearTerminal()
    else:
        AppUI.MainLoop()

    return 0

# ---------------------------------------

if __name__ == "__main__":
    main()