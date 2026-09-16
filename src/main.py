# Import Statements
import app as App
import subprocess, platform

# This function's entire job is to clear the terminal based on the operating system for easier viewing.
def ClearTerminal() -> None:
    if (platform.system().lower() == 'windows'): subprocess.run('cls', shell=True)
    else: subprocess.run('clear', shell=True)

# Main Program Loop
def main() -> int:
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

    return 0

if __name__ == "__main__":
    main()