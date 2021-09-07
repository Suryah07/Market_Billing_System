from tkinter import *
import database
#to add items to the inventory from the entry box
def addinventory():
    idvalue = id.get()
    namevalue = name.get()
    ratevalue = rate.get()
    database.add_item(idvalue,namevalue,ratevalue)
    idplace()
    nameplace()
    rateplace()

def removeinventory():
    namevalue = name.get()
    idvalue = id.get()
    ratevalue = rate.get()
    database.remove_item(namevalue)
    idplace()
    nameplace()
    rateplace()

def idplace():
    items = database.selectall()
    id_box.delete(0,END)
    for x in items:
        id_box.insert(0,x[0])

def nameplace():
    names = database.selectall()
    name_box.delete(0,END)
    for x in names:
        name_box.insert(0,x[1])

def rateplace():
    rates = database.selectall()
    rate_box.delete(0,END)
    for x in rates:
        rate_box.insert(0,x[2])

#def create():
root = Tk()
root.title('INVENTORY')
root.geometry('1920x1080')
bg_color = '#2D9290'
title = Label(root,text = 'INVENTORY',bg=bg_color,fg = 'white',font =('times new romman',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill = X)

#<<<<<<<<<<<<<<<<<<<<<DISPLAYS>>>>>>>>>>>>>>>>>>>>>>
idlab = Label(root, text="ID",font=("times new romman", 14))
idlab.place(x=850,y=120)
id_box = Listbox(root,width = 40,height = 20,font=("Helvetica"))
id_box.place(x=800,y = 150)
idplace()

namelab = Label(root, text="NAME",font=("times new romman", 14))
namelab.place(x=1000,y=120)
name_box = Listbox(root,width = 40,height = 20,font=("Helvetica"))
name_box.place(x=900,y = 150)
nameplace()

ratelab = Label(root, text="RATE",font=("times new romman", 14))
ratelab.place(x=1320,y=120)
rate_box = Listbox(root,width = 40,height = 20,font=("Helvetica"))
rate_box.place(x=1200,y = 150)
rateplace()

#<<<<<<<<<<<<<<<<<<<<<<<<ENTRIES>>>>>>>>>>>>>>>>>>>>>>>
idlab = Label(root, text="ID",font=("times new romman", 14))
idlab.place(x=120,y=120)
id = Entry(root,font=("Helvetica"),width=10)
id.place(x=80,y=150)

namelab = Label(root, text="NAME",font=("times new romman", 14))
namelab.place(x=325,y=120)
name = Entry(root,font=("Helvetica"),width=25)
name.place(x=210,y=150)

ratelab = Label(root, text="RATE",font=("times new romman", 14))
ratelab.place(x=540,y=120)
rate = Entry(root,font=("Helvetica"),width=10)
rate.place(x=507,y=150)

add_to_inventory = Button(text = "Add To Inventory",command=addinventory,height=3,width=20,font=("Helvetica"))
add_to_inventory.place(x=230,y=200)

remove_from_inventory = Button(text = "Remove From Inventory",command=removeinventory,height=3,width=20,font=("Helvetica"))
remove_from_inventory.place(x=230,y=300)

#Dont know why but the display is working without this
root.mainloop()