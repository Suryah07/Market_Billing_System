import config as details
import mysql.connector
def create_table():
    mycursor.execute("create table items (id int,name varchar(25),rate int);")

#To check weather the connection is correct
try:
    mydb = mysql.connector.connect(host=details.host,user=details.username,password=details.userpass,database=details.database)
    mycursor = mydb.cursor()
    #To check weather there is table in the name items or not
    try:
        mycursor.execute("SELECT * FROM items;")
        abc = mycursor.fetchall()
    except:
        print("The credentials given by you are correct but there is no table in that database.")
        print("Enter 1. To create a table named items")
        print("Enter 2. To exit...")
        option = int(input())
        if(option == 1):
            create_table()
        else:
            print("Ok bye...")
            input()
except mysql.connector.Error:
    
    print("The credentials stored in config.py are invalid. Kindly check and try again")
    input()

#This function is used to return the items in the inventory
def item_list():
    items = []
    cmd = "SELECT * FROM  items;"
    mycursor.execute(cmd)
    result = mycursor.fetchall()
    for x in result:
        items.append(x[1])    
    return items

#This function is used to return the rate of the items in the inventory
def item_rate(name):
    rate = []
    cmd = "SELECT RATE FROM ITEMS WHERE NAME = %s;"
    mycursor.execute(cmd,(name,))
    result = mycursor.fetchall()
    #for x in result:
    #rate.append(x[2])
    rate = result
    return rate

#To insert the items to the table
def add_item(id,name,rate):
    cmd = "insert into items (id,name,rate) values (%s,%s,%s);"
    mycursor.execute(cmd,(id,str(name),rate,))
    return

#to select all the values and return in a type of list
def selectall():
    mycursor.execute("SELECT * FROM items;")
    allthis = mycursor.fetchall()
    mydb.commit()
    return allthis

def remove_item(name):
    cmd = "DELETE FROM items WHERE name = %s;"
    mycursor.execute(cmd,(name,))

def save_bill(name):
    print("hello")
    
