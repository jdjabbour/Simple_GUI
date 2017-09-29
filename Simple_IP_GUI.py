import socket
import ipaddr
import urllib
from tkinter import *

root = Tk()

def find_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    x = s.getsockname()[0]
    mask = ipaddr.IPv4Network(x)
    y = mask.netmask
    t1.insert(END, x)
    t2.insert(END, y)
    s.close()

def public_info():
    ip = urllib.urlopen('http://wtfismyip.com/json').read()
    a = [i for i in ip.split()]
    ip_add = re.findall(r'[0-9]{1,2}\W[0-9]{1,3}\W[0-9]{1,3}\W[0-9]{1,}', a[2])
    t3.insert(END, ip_add)
    city = a[4]
    state = a[5]
    country1 = a[6]
    country2 = a[7]
    loc = city + " " + state + " " + country1 + " " + country2
    t4.insert(END, loc)
    t5.insert(END, a[9])
    isp1 = a[11]
    isp2 = a[12]
    isp3 = a[13]
    isp = isp1 + " " + isp2 + " " + isp3
    t6.insert(END, isp)

l1 = Label(root, text="Local IP")
l1.pack()

t1 = Text(root, height=1, width=40)
t1.pack()

l2 = Label(root, text="Subnet Mask")
l2.pack()

t2 = Text(root, height=1, width=40)
t2.pack()

b1 = Button(root, text="Find Local IP", command=find_ip)
b1.pack()

l3 = Label(root, text="Public IP")
l3.pack()

t3 = Text(root, height=1, width=40)
t3.pack()

l4 = Label(root, text="Location")
l4.pack()

t4 = Text(root, height=1, width=40)
t4.pack()

l5 = Label(root, text="Host Name")
l5.pack()

t5 = Text(root, height=1, width=40)
t5.pack()

l6 = Label(root, text="ISP")
l6.pack()

t6 = Text(root, height=1, width=40)
t6.pack()



b2 = Button(root, text="Find Public Info", command=public_info)
b2.pack()

root.mainloop()