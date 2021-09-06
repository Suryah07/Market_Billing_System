import config
import mysql.connector
def create_table():
    mycursor.execute("create table items (id int,name varchar(25),rate int);")
try:
    mydb = mysql.connector.connect(host=config.host,user=config.username,password=config.userpass,database=config.database)
    mycursor = mydb.cursor()
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
except mysql.connector.Error:
    print("The credentials stored in config.py are invalid. Kindly check and try again")


        #exit

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
def add_item():
    return

