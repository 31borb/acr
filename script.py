import pyautogui
import threading
import appJar
import mouse
import keyboard

app = appJar.gui("acr ")
app.setSize("300x300")
app.setSticky("new")
app.setSticky("e")
app.addLabel("Hold to", row=0)
app.radioButton("onoff", "off", row=1, column=0)
app.radioButton("onoff", "on", row=1, column=2)

def clicker():
    onoff = app.radioButton("onoff")
    if(onoff == "on"):
        while True:
            while mouse.is_pressed(button="left") == True:
                pyautogui.click(button="left", interval=0.1)
            if(onoff == "off"):
                while True:
                    while mouse.is_pressed(button="right") == True:
                        pyautogui.click(button="right", interval=0.1)

for i in range(6):
    thread = threading.Thread(target=clicker)
    thread.start()

def checkStop():
    if keyboard.is_pressed("ESC"):
        return app.yesNoBox("Confirm Exit", "Are you sure you want to exit?")
    app.setStopFunction(checkStop)

app.go()