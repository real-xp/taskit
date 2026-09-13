import app as App
import subprocess, platform

def ClearTerminal():
    if (platform.system().lower() == 'windows'): subprocess.run('cls', shell=True)
    else: subprocess.run('clear', shell=True)

def main() -> int:
    app = App.App()
    app.PrintHelp()
    
    while (True):
        app.ShowCurrentMenu()
        userInput = [*map(str, str(input("What Operation Do You Want To Perform? : ")).lower().lstrip().split(";"))]
        argResult = app.ArgParse(userInput=userInput)
        if (argResult in (1, -1)):
            break

        input("Press Any Key To Continue\n\n")
        ClearTerminal()

    return 0

if __name__ == "__main__":
    main()