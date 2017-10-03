from tkinter import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Trouble Shooter")
        self.pack(fill=BOTH, expand=1)

def vpntshoot():
    text.delete(1.0, END)
    vpnA = e1.get()
    vpnB = e2.get()
    vpnC = e3.get()
    vpnD = e4.get()
    text.insert(END, vpnA)
    text.insert(END, vpnB)
    text.insert(END, vpnC)
    text.insert(END, vpnD)

root = Tk()

label1 = Label(root, text="Source IP Address")
e1 = Entry(root, bd=5)

label2 = Label(root, text="Destination IP Address")
e2 = Entry(root, bd=5)

label3 = Label(root, text="Source Port")
e3 = Entry(root, bd=5)

label4 = Label(root, text="Desination Port")
e4 = Entry(root, bd=5)


label1.pack()
e1.pack()
label2.pack()
e2.pack()
label3.pack()
e3.pack()
label4.pack()
e4.pack()

vpn = Button(root, text="VPN TSHOOT", comman=vpntshoot)
vpn.pack()

text = Text(root)
text.pack()

app = Window(root)
root.mainloop()