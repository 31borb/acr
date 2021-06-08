import pyautogui
import threading
import appJar
import mouse
import keyboard

def clicker():
        toClick = app.radioButton("toClick")
        if(toClick == "Left Click"):
            toClick = "left"
        else:
            toClick = "right"
        while True:
            while mouse.is_pressed(button=toClick) == True:
                pyautogui.click(button=toClick, interval=0.1) 

for i in range(3):
    thread = threading.Thread(target=clicker)
    thread.start()

app = appJar.gui("acr")
app.setSize("300x300")
app.setSticky("new")
app.setSticky("e")
app.addLabel("Hold to start", row=0)
app.setSticky("e")
app.radioButton("toClick", "Right Click", row=1)
app.setSticky("w")
app.radioButton("toClick", "Left Click", row=1)

app.go()
