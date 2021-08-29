#inporting libraries
from tkinter import *
root = Tk()
root.title('Billing System')
root.geometry('1920x1080')
bg_color = '#2D9290'
title = Label(root,text = 'Billing System',bg=bg_color,fg = 'white',font =('times new romman',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill = X)

#==============PRODUCT DETAILS==================

#add the item to the bill
def additem():
    print(typed_text)
    #product.delete(1,END)




# Update the listbox
def update_listbox(data):
  # Clear the listbox
  list_box.delete(0, END)

  # Add programming_lan to listbox
  for item in data:
    list_box.insert(END, item)

# Update entry box with listbox clicked
def update(e):
  # Delete entry box
  product.delete(0, END)

  # Add clicked list item to entry box
  product.insert(0, list_box.get(ANCHOR))

# Check entry box vs listbox
def check(e):
  # get typed text
  global typed_text
  typed_text = product.get()

  if typed_text == '':
    data = programming_lan
  else:
    data = []
    for item in programming_lan:
      if typed_text.lower() in item.lower():
        data.append(item)

  # update our listbox
  update_listbox(data)        

# Create a label
Searchlab = Label(root, text="Search",font=("times new romman", 14))
Searchlab.place(x=400,y=120)
Quantitylab = Label(root, text="Quantity",font=("times new romman", 14))
Quantitylab.place(x=900,y=120)

# Create an entry box
product = Entry(root, font=("Helvetica"),width=70)
product.place(x=60,y=150)

quantity = Entry(root,font=("Helvetica"),width=10)
quantity.place(x=900,y=150)

# Create a listbox
list_box = Listbox(root, width=100)
list_box.place(x=60,y=190)

# Programming Language List
programming_lan = ["Python","Javascript","C++","Java","PHP","Kotlin","Suryah","apple","suryah12","adventure","windows","macos"]

# Add the programming_lan to our list
update_listbox(programming_lan)

# Create a binding on the listbox
list_box.bind("<<ListboxSelect>>", update)

# Create a binding on the entry box
product.bind("<KeyRelease>", check)

addbutton = Button(text="Add Item",command=additem)
addbutton.place(x=1050,y=150)



#execute tkinter
root.mainloop()