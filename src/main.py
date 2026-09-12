import app as App

def main() -> int:
    app = App.App()
    app.PrintHelp()
    
    while (True):
        userInput = [*map(str, str(input("What Operation Do You Want To Perform? : ")).lower().lstrip().split(";"))]
        argResult = app.ArgParse(userInput=userInput)
        if (argResult in (1, -1)):
            break

    return 0

if __name__ == "__main__":
    main()