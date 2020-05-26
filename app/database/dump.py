import os
import threading
import time

import mysql.connector

from dotenv import load_dotenv

time.sleep(20)

load_dotenv()


cnx = mysql.connector.connect(user="admin_delegate", password="admin_delegate",
                              host="localhost", database="devops")

cursor = cnx.cursor(buffered=True)


def generate_file():
    datetime = time.strftime('%d-%m-%Y-%H%M%S')
    filename = datetime + ".sql"
    file = open(filename, "x")
    os.system("mysqldump --databases devops -u admin_delegate --password=admin_delegate --single-transaction >" + filename)
    threading.Timer(os.environ["BACK_UP_TIME"], generate_file).start()


generate_file()
