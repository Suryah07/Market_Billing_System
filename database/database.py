import config
import mysql.connector
con = mysql.connector.connect(host=config.host,user=config.username,password=config.userpass,database=config.database)
