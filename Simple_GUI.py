from tkinter import *


root = Tk()

def set_var():
    var = (e1_value.get())  # Uses the get method to
    t1.insert(END, var)  # Takes the string from the entry object and prints it in the text object

# The entry takes the text as a string and awaits for the button to be pressed
e1_value = StringVar()  # Established the text entered into the entry box is a string
e1 = Entry(root, textvariable=e1_value)  # Establishes the variable from the string entered
e1.pack()

# Outputs the string in the text box
t1 = Text(root, height=1, width=20)
t1.pack()

# Takes the string entered in the entry window and calls the function
button1 = Button(root, text="Click me", command=set_var)
button1.pack()



root.mainloop()
