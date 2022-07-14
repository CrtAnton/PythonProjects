from tkinter import *
import pydirectinput
import keyboard

window = Tk()
window.geometry("250x225")
window.resizable(False, False)
window.title("Clicker")

lbl = Label(window, text = "Set speed(1-20)")
lbl.pack(pady = 10)
txt_speed = Entry(window)
txt_speed.pack()
lbl = Label(window, text = "Set stop key")
lbl.pack(pady = 10)
txt_stop = Entry(window)
txt_stop.pack()

def start():
    lbl_warning.configure(text= "" )
    if int(txt_speed.get()) >20 or int(txt_speed.get())<1:
        lbl_warning.configure(text= "Set the speed right" )
        return
    while True:      
        pydirectinput.click(clicks = int(txt_speed.get()))
        if keyboard.is_pressed(txt_stop.get()):
            break
            
btn = Button(window, text="Start", command=start)
btn.pack(pady=10)
lbl_warning = Label(window)
lbl_warning.pack()

window.mainloop()
