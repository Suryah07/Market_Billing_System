#inporting libraries
from tkinter import *
import database
root = Tk()
root.title('Billing System')
root.geometry('1920x1080')
bg_color = '#2D9290'
title = Label(root,text = 'Billing System',bg=bg_color,fg = 'white',font =('times new romman',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill = X)

#==============PRODUCT DETAILS==================

#add the item to the bill and give output of the bill
def additem():
    bill_list.append(typed_text)
    i = additem.counter
    bill_box.insert(0,(bill_list[i]))
    addrate(typed_text)
    additem.counter = additem.counter+1

additem.counter = 0

#Used to print the rate of the item in the rate box
def addrate(name):
    item_rate = database.item_rate(name)
    rate_box.insert(0,item_rate)    
    item_rateee = num = list(sum(item_rate, ()))
    addprice(int(item_rateee[0]))

#used to print the price after calculating the rate and the quantity 
def addprice(item_rate):
  quanty = int(quantity.get())
  quantity_box.insert(0,quanty)
  price = item_rate*quanty
  price_box.insert(0,price)
  price_list.append(price)
  total(price_list)

def total(price_list):
  sum = 0
  for x in price_list:
    sum = sum+x
  tot_box.delete(0,END)
  tot_box.insert(0,sum)


# Update the listbox
def update_listbox(data):
  # Clear the listbox
  list_box.delete(0, END)

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

# Create a label for search
Searchlab = Label(root, text="Search",font=("times new romman", 14))
Searchlab.place(x=400,y=120)

#Create a label for quantity
Quantitylab = Label(root, text="Quantity",font=("times new romman", 14))
Quantitylab.place(x=900,y=120)

#Create a lable for name
namelab = Label(root,text="ITEM",font =("times new romman",14))
namelab.place(x=530,y=189)

#create a lable for rate
ratelab = Label(root,text="RATE",font =("times new romman",14))
ratelab.place(x=730,y=189)

#Create a lable for quantity
quantitylab = Label(root,text="QUANTITY",font=("times new romman",14))
quantitylab.place(x=940,y=189)

#create a lable for price
pricelab = Label(root,text="PRICE",font =("times new romman",14))
pricelab.place(x=1170,y=189)

#create a lable for total
totlab = Label(root,text="TOTAL",font =("times new romman",14))
totlab.place(x=1360,y=620)

# Create an entry box for product
product = Entry(root, font=("Helvetica"),width=70)
product.place(x=60,y=150)

#Create an entry box for quantity
quantity = Entry(root,font=("Helvetica"),width=10)
quantity.place(x=900,y=150)

# Create a listbox
list_box = Listbox(root, width=50)
list_box.place(x=60,y=190)

#Creating a list to store the items in the bill
bill_list =[]

#Creating a list to store the rate of the items in the bill
rate_list =[]

#Creating a list to store the proce of the items in the bill
price_list =[]

#Creating a list box display the bill
bill_box = Listbox(root,width=50,height=30,)
bill_box.place(x=450,y=230)

#bill_box.insert(1,"Suryah")
rate_box = Listbox(root,width = 50,height = 30,)
rate_box.place(x=660,y = 230)

quantity_box = Listbox(root,width = 50,height = 30,)
quantity_box.place(x=870,y = 230)

#price box to display total price
price_box = Listbox(root,width = 40, height = 30,)
price_box.place(x =1080,y= 230)

#total box to display the total of the bill
tot_box = Listbox(root,width = 30, height = 3,)
tot_box.place(x =1325,y= 660)

# Programming Language List
programming_lan = database.item_list()

# Add the programming_lan to our list
update_listbox(programming_lan)

# Create a binding on the listbox
list_box.bind("<<ListboxSelect>>", update)

# Create a binding on the entry box
product.bind("<KeyRelease>", check)

#Adding a button to add the selected item to the bill of the customer
addbutton = Button(text="Add Item",command=additem)
addbutton.place(x=1050,y=150)

#execute tkinter
root.mainloop()