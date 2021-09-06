import config
import mysql.connector


mydb = mysql.connector.connect(host=config.host,user=config.username,password=config.userpass,database=config.database)
mycursor = mydb.cursor()
#This function is used to return the items in the inventory
def item_list():
    items = []
    mycursor.execute("SELECT * FROM ITEMS;")
    result = mycursor.fetchall()
    for x in result:
        items.append(x[1])    
    return items
#This function is used to return the rate of the items in the inventory
def item_rate(name):
    rate = []
    print(name)
    cmd = "SELECT RATE FROM ITEMS WHERE NAME = %s;"
    mycursor.execute(cmd,(name,))
    result = mycursor.fetchall()
    #for x in result:
    #rate.append(result[2])
    x = result
    return x
def add_item():
    return