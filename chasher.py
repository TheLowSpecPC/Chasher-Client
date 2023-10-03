from tkinter import *
from functools import partial
import os
import insert,remove

cwd = os.getcwd()

root = Tk()
root.geometry("700x300")
root.resizable(width=False, height=False)
root.title("Chasher Client (Made By: The Low Spec PC)")
root.iconbitmap(cwd+"/icon.ico")
root.config(bg="gray")

def host():
    with open('host.txt', 'w') as c:
        c.write(h.get())
        c.close()

def money(no):
    with open('host.txt', 'r') as d:
        client_link = d.readline()
        d.close()
    name = a.get()
    amount = int(b.get())
    if no == 1:
        line = insert.run(client_link,name,amount)
    elif no == 0:
        line = remove.run(client_link,name,amount)
    cmd.insert(END, line)
    cmd.see("end")

def temp_text1(e):
    a.delete(0,"end")
def temp_text2(e):
    b.delete(0,"end")

Label(root, text="Chasher Client", font=("Raleway", 20), bg="black", fg="white", height="1").place(x=265, y=1)

Label(root, text="Host Link:", font=("Raleway", 16), bg="black", fg="white", height="1").place(x=160, y=60)
h = Entry(root, width="30")
h.place(x=270, y=65)
with open('host.txt', 'r') as c:
    link = c.readline()
    c.close()
h.insert(0, link)
Button(root, text="Save", command=host, width="5", height="1").place(x=470, y=60)

Label(root, text="Name", font=("Raleway", 18), bg="black", fg="white", height="1").place(x=260, y=110)
a = Entry(root, width="26")
a.insert(0, "Eg: 12A45ALENROYTHOMAS")
a.place(x=220, y=160)
a.bind("<FocusIn>", temp_text1)

Label(root, text="Amount", font=("Raleway", 18), bg="black", fg="white", height="1").place(x=400, y=110)
b = Entry(root, width="10")
b.insert(0, "Amount")
b.place(x=410, y=160)
b.bind("<FocusIn>", temp_text2)

Button(root, text="Add Money", command=partial(money, 1), width="12", height="1").place(x=250, y=200)
Button(root, text="Subtract Money", command=partial(money, 0), width="12", height="1").place(x=380, y=200)

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")
cmd = Text(root, width="83", height="3")
cmd.place(x=10, y=230)
scrollbar.config(command=cmd.yview)
cmd.config(yscrollcommand=scrollbar.set)

root.mainloop()