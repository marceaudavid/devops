import os
import threading
import time

import mysql.connector

from dotenv import load_dotenv

load_dotenv()

USER = os.environ['MYSQL_ADMIN_DELEGATE_USER']
PASSWORD = os.environ['MYSQL_ADMIN_DELEGATE_USER_PASSWORD']
HOST = os.environ['MYSQL_HOST']
DATABASE = os.environ['MYSQL_DATABASE']

BACK_UP_TIME = 86400.0  # DEFAULT 86400 = 1 Day backup

cnx = mysql.connector.connect(user="admin_delegate", password="admin_delegate",
                              host="localhost", database="devops")

cursor = cnx.cursor(buffered=True)


def generate_file():
    datetime = time.strftime('%d-%m-%Y-%H%M%S')
    filename = datetime + ".sql"
    file = open(filename, "x")
    dump = "mysqldump -h " + HOST + " -P 3306" + \
        " -u " + USER + " " + DATABASE + ' > ' + filename
    threading.Timer(10, generate_file).start()


generate_file()
