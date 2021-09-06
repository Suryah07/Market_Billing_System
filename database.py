import config
import mysql.connector
from .main import Layout

con = mysql.connector.connect(host=config.host,user=config.username,password=config.userpass,database=config.database)
