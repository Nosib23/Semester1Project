from tkinter import *

# constants
CHEAP = 0.4
EXPENSIVE = 0.75
BOW = 1.5
GIFT_CARD = 0.5
CHARS = 0.02

mainWindow = Tk()
mainWindow.title("Order system")

title = Label(mainWindow, text="Ordering System", font=("Arial", 20, "bold"))
title.grid(column=0, row=1, columnspan=2)

paperTypeLbl = Label(mainWindow, text="Which paper should be used?")
paperTypeLbl.grid(column=0, row=2)

paperChoice = IntVar()
cheapPaper = Radiobutton(mainWindow, text="Cheap paper", variable=paperChoice, value=1)
expPaper = Radiobutton(mainWindow, text="Expensive paper", variable=paperChoice, value=2)
cheapPaper.grid(column=1, row=2)
expPaper.grid(column=1, row=3)

boxButton = Button(mainWindow, text="Box", command=box())
cylinderButton = Button(mainWindow, text="Cylinder", command=cylinder())

def box():
    pass

def cylinder():
    pass

dimensionsLbl = Label(mainWindow, text="Dimensions:")
dimensionsLbl.grid(column=0, row=5)

heightLbl = Label(mainWindow, text="Height:")
heightEntry = Entry(mainWindow)
widthLbl = Label(mainWindow, text="Width:")
widthEntry = Entry(mainWindow)
depthLbl = Label(mainWindow, text="Depth:")
depthEntry = Entry(mainWindow)

heightLbl.grid(column=0, row=6)
heightEntry.grid(column=1, row=6)
widthLbl.grid(column=0, row=7)
widthEntry.grid(column=1, row=7)
depthLbl.grid(column=0, row=8)
depthEntry.grid(column=1, row=8)

mainWindow.mainloop()