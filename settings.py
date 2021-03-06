from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as font
import pyautogui
import time

fontSetup = ('Arial', 15)

def insertCommand(window, listbox, type, cmd):
    cmd = cmd[0:len(cmd)-1]
    # pos = cmd.split()
    listbox.insert(END, type + ' ' + cmd)
    close(window)

def close(window):
    window.destroy()

def getCursorPosition(event, positionXY):
    positionXY.delete(1.0, END)
    positionXY.insert(1.0, pyautogui.position())

def clicker(root, listbox):
    clickerWindow = Toplevel(root)
    clickerWindow.title("👆 Clicker")
    clickerWindow.geometry("450x220")
    clickerWindow.resizable(False, False)
    buttonLabel = Label(clickerWindow, text="Button: ", font=fontSetup)
    buttonType = ttk.Combobox(clickerWindow, values=["Left", "Right"], font=fontSetup)
    buttonType.set("Left")
    positionLabel = Label(clickerWindow, text="Position: ", font=fontSetup)
    positionXY = Text(clickerWindow, width=10, height=1.5)
    positionButton = Button(clickerWindow, text="+", font=fontSetup)
    positionButton.bind('<ButtonRelease-1>', lambda event:getCursorPosition(event, positionXY))
    amountLabel = Label(clickerWindow, text="Amount: ", font=fontSetup)
    amountOfClicks = Text(clickerWindow, width=10, height=1.5)
    cancelButton = Button(clickerWindow, text="Cancel", command=lambda:close(clickerWindow))
    okButton = Button(clickerWindow, text="OK", command=lambda:insertCommand(clickerWindow, listbox, "👆", (positionXY.get(1.0, END) + ' ' + amountOfClicks.get(1.0, END))))
    buttonLabel.grid(row=1, column=0, sticky=W)
    buttonType.grid(row=1, column=1, columnspan=2, sticky=E)
    positionLabel.grid(row=2, column=0, sticky=W)
    positionXY.grid(row=2, column=1, sticky=E)
    positionButton.grid(row=2, column=2, sticky=E)
    amountLabel.grid(row=3, column=0, sticky=W)
    amountOfClicks.grid(row=3, column=1, sticky=W)
    cancelButton.grid(row=4, column=0, sticky=E)
    okButton.grid(row=4, column=1, sticky=E)

def moveCursor(root, listbox):
    cursorWindow = Toplevel(root)
    cursorWindow.title("👣 Move Cursor")
    cursorWindow.geometry("450x220")
    cursorWindow.resizable(False, False)
    buttonLabel = Label(cursorWindow, text="Button: ", font=fontSetup)
    buttonType = ttk.Combobox(cursorWindow, values=["Left", "Right"], font=fontSetup)
    buttonType.set("Left")
    positionLabel = Label(cursorWindow, text="Position: ", font=fontSetup)
    positionXY = Text(cursorWindow, width=10, height=1.5)
    positionButton = Button(cursorWindow, text="+", font=fontSetup)
    positionButton.bind('<ButtonRelease-1>', lambda event:getCursorPosition(event, positionXY))
    amountLabel = Label(cursorWindow, text="Amount: ", font=fontSetup)
    cancelButton = Button(cursorWindow, text="Cancel", command=lambda:close(clickerWindow))
    okButton = Button(cursorWindow, text="OK", command=lambda:insertCommand(clickerWindow, listbox, "👆", positionXY.get(1.0, END)))
    buttonLabel.grid(row=1, column=0, sticky=W)
    buttonType.grid(row=1, column=1, columnspan=2, sticky=E)
    positionLabel.grid(row=2, column=0, sticky=W)
    positionXY.grid(row=2, column=1, sticky=E)
    positionButton.grid(row=2, column=2, sticky=E)
    amountLabel.grid(row=3, column=0, sticky=W)
    cancelButton.grid(row=4, column=0, sticky=E)
    okButton.grid(row=4, column=1, sticky=E)
    # pyautogui.moveTo(x, y)

def pause(root, listbox):
    pauseWindow = Toplevel(root)
    pauseWindow.title("⏳ Pause")
    pauseWindow.geometry("450x220")
    pauseWindow.resizable(False, False)
    listbox.insert(END, "Pause")
    # time.sleep(1)

def openWindow(root, window, title):
    window = Toplevel(root)
    window.title(title)
    window.geometry("450x220")
    window.resizable(False, False)