import items
from guizero import App, Text, PushButton, Window, Picture, TextBox, error, ListBox, yesno
global ID
global ListboxList
ListboxList = []
def EatenFood():
    print("EatenFood")



    
def RecipesFunction():
    print("Recipes")



    
def CheckExpiry():
    CheckExpiryWindow = Window(app,width = 450,height = 550, title = "Fridge Contents",bg = "#9cdaf6")
    CheckExpiryWindow.show(wait= True)
    picture = Picture(CheckExpiryWindow, image  = "ExtraSmall.png")
    ListboxList = items.start(IDEntry.get())
    print(ListboxList)
    listbox = ListBox(CheckExpiryWindow,items = ListboxList,width = 48,height = 18)
    Delete = PushButton(CheckExpiryWindow,width = 54,command = RecipesFunction, text = "DELETE ITEM",grid = [1,4,2,1],pady = 14)






def DisplayMain():
    app.hide()
    Mainwindow = Window(app,width = 450,height = 550,layout = "grid", title = "Main Menu",bg = "#9cdaf6")
    Mainwindow.show()
    Text(Mainwindow, text = "    ",grid = [0,0])
    picture = Picture(Mainwindow, image  = "ExtraSmall.png",grid = [1,0,2,1])
    
    Text(Mainwindow, text = "Welcome, Please Choose One Of The Following Options",grid = [1,2,2,1])
    Text(Mainwindow,text = "", grid = [0,3],size =4)
    CheckExpireButton = PushButton(Mainwindow,width = 54,command = CheckExpiry, text = "Check Expiry Dates",grid = [1,4,2,1],pady = 14)
    Text(Mainwindow,text = "",grid = [0,5],size =4)
    FoodEatenButton = PushButton(Mainwindow, text = "Food Eaten",width = 24,align = "left", grid = [1,6],pady = 15)
    
    RecipesButton = PushButton(Mainwindow, text = "Recipes",width = 24,align = "right", grid = [2,6],pady = 15)

    Text(Mainwindow,text = "",grid = [0,7],size =4)

    
    ExitButton = PushButton(Mainwindow, text = "Exit",width = 54, grid = [1,8,2,1],command = lambda: Mainwindow.destroy())
    ExitButton.bg = "#ce2029"
    ExitButton
    
def MainMenu():
    UserCheck = False
    users = open("users.csv", "r")
    userlist = []
    for item in users:
        userlist.append(item.split(","))
    for item in userlist:
        if item[0] == IDEntry.get():
            UserCheck = True
            ID = IDEntry.get()
            break
        else:
            continue
        
    if UserCheck == True:
        DisplayMain()
    else:
        error("Incorrect Login", "Please Enter A Correct User ID")

def ClearText():
    global TextCheck
    if TextCheck == 0:
        IDEntry.clear()
        TextCheck = TextCheck + 1
global TextCheck
TextCheck = 0
app = App( title=" ID Entry",bg = "#9cdaf6",width = 450,height = 550)
picture = Picture(app, image = "Small.png")
message = Text(app, text = "Welcome, Please Scan Or Enter Your ID")
IDEntry = TextBox(app, text = "\tPlease Enter Here", width = 30)


IDEntry.when_clicked = ClearText

LoginButton = PushButton(app, command = MainMenu, text = "Login")

app.display()

#message = Text(Mainwindow, text = "Welcome, Please Choose One Of The Following Options",grid = [1,2])
