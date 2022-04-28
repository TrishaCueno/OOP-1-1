#Create a program to produce the interface. Click the button to chnage its background color to yellow.

from tkinter import *
window = Tk()

window.geometry('450x350')
window.title("Special Midterm Exam in OOP")

button = Button(window, text="Click to Change Color", bg="#ffffff", activebackground="#ffff00")
button.place(x=165, y=165)

window.mainloop()