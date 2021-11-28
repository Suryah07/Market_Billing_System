#inporting libraries
from tkinter import *
#import inventory
import database
import xlsxwriter
from tkinter import simpledialog




root = Tk()
root.title('Billing System')
root.geometry('1920x1080')
bg_color = '#2D9290'
title = Label(root,text = 'Billing System',bg=bg_color,fg = 'white',font =('times new romman',35,'bold'),relief=GROOVE,bd=12)
title.pack(fill = X)

#==============PRODUCT DETAILS==================

def printbill():
  print("hi")
  cname = simpledialog.askstring(title="Bill Save",prompt="Customer name")
  workbook = xlsxwriter.Workbook("Bills/"+cname+".xlsx")
  worksheet = workbook.add_worksheet()
  row = 0
  col = 0

  for a in bill_box.get(0,END):
    worksheet.write(row,col,a)
    row = row+1
  col = col+1
  row = 0

  for a in rate_box.get(0,END):
    worksheet.write(row,col,a[0])
    row = row+1
  col = col+1
  row = 0

  for a in quantity_box.get(0,END):
    worksheet.write(row,col,a)
    row = row+1
  col = col+1
  row = 0

  for a in price_box.get(0,END):
    worksheet.write(row,col,a)
    row = row+1
  col = col+1

  for a in tot_box.get(0,END):
    worksheet.write(row,col,"Total")
    col = col+1
    worksheet.write(row,col,a)
    row = row+1

  col = col+1
  row = 0

  tot_box.delete(0,END)
  price_box.delete(0,END)
  rate_box.delete(0,END)
  bill_box.delete(0,END)
  quantity_box.delete(0,END)
  gsum = 0
  price_list.clear
  rate_list.clear
  bill_list.clear
  tot_box.insert(0,gsum)

  workbook.close()
  



def close():
  root.destroy()
  import inventory
  return

#add the item to the bill and give output of the bill
def additem():
    item_adding = product.get()
    typed_text = item_adding
    bill_list.append(typed_text)
    i = additem.counter
    bill_box.insert(0,(bill_list[i]))
    addrate(typed_text)
    additem.counter = additem.counter+1

additem.counter = 0

#Used to print the rate of the item in the rate box
def addrate(name):
    item_rate = database.item_rate(name)
    rate_box.insert(0,item_rate[0])    
    item_rateee = list(sum(item_rate, ()))
    addprice(int(item_rateee[0]))

#used to print the price after calculating the rate and the quantity 
def addprice(item_rate):
  quanty = int(quantity.get())
  quantity_box.insert(0,quanty)
  price = item_rate*quanty
  price_box.insert(0,price)
  price_list.append(price)
  total(price_list,price)

def total(price_list,price):
  global gsum
  gsum = 0
  tsum = tot_box.get(0,0)
  tsum = tsum[0]+price
  #for x in price_list:
    #gsum = gsum+x
  tot_box.delete(0,END)
  tot_box.insert(0,tsum)


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
    data = items_in_base
  else:
    data = []
    for item in items_in_base:
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
namelab.place(x=540,y=209)

#create a lable for rate
ratelab = Label(root,text="RATE",font =("times new romman",14))
ratelab.place(x=740,y=209)

#Create a lable for quantity
quantitylab = Label(root,text="QUANTITY",font=("times new romman",14))
quantitylab.place(x=950,y=209)

#create a lable for price
pricelab = Label(root,text="PRICE",font =("times new romman",14))
pricelab.place(x=1180,y=209)

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
list_box = Listbox(root, width=30,font=("Helvetica"))
list_box.place(x=60,y=190)

#Creating a list to store the items in the bill
global bill_list
bill_list =[]

#Creating a list to store the rate of the items in the bill
global rate_list
rate_list =[]

#Creating a list to store the proce of the items in the bill
global price_list
price_list =[]

#Creating a list box display the bill
bill_box = Listbox(root,width=20,height=15,font=("Helvetica"))
bill_box.place(x=460,y=250)

#bill_box.insert(1,"Suryah")
rate_box = Listbox(root,width = 20,height = 15,font=("Helvetica"))
rate_box.place(x=670,y = 250)

quantity_box = Listbox(root,width = 20,height = 15,font=("Helvetica"))
quantity_box.place(x=880,y = 250)

#price box to display total price
price_box = Listbox(root,width = 20, height = 15,font=("Helvetica"))
price_box.place(x =1090,y= 250)

#total box to display the total of the bill
tot_box = Listbox(root,width = 16, height = 3,font=("Helvetica"))
tot_box.place(x =1325,y= 660)
tot_box.insert(0,0)

# Programming Language List
items_in_base = database.item_list()

# Add the programming_lan to our list
update_listbox(items_in_base)

# Create a binding on the listbox
list_box.bind("<<ListboxSelect>>", update)

# Create a binding on the entry box
product.bind("<KeyRelease>", check)

#Adding a button to add the selected item to the bill of the customer
addbutton = Button(text="Add Item",command=additem,font=("Helvetica"))
addbutton.place(x=1050,y=145)

billbutton = Button(text = "Print Bill",command =printbill,font=("Helvetica"))
billbutton.place(x=1070,y=650)

#Addding button to manage inventory
inventory_button = Button(text = "Manage Inventory",command=close,height=5,width=20,font=("Helvetica"))
inventory_button.place(x=100,y=650)

#execute tkinter
root.mainloop()
