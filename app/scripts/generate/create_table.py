import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',
                              database='devops')

cursor = cnx.cursor()

cursor.execute(
    "CREATE TABLE units (id INT AUTO_INCREMENT PRIMARY KEY, robot_number INT);")

cursor.execute(
    "CREATE TABLE robots (id INT AUTO_INCREMENT PRIMARY KEY, unit_number INT NOT NULL, robot_number INT NOT NULL, robot_type VARCHAR(12) NOT NULL, tank_temperature INT NOT NULL, external_temperature INT NOT NULL, weight_of_milk_in_tank INT NOT NULL, weight_of_milk_difference INT NOT NULL, ph_measure INT NOT NULL, k_measure INT NOT NULL, nacl_concentration INT NOT NULL, salmonella_bacterium_level INT NOT NULL, e_coli_bacterium_level INT NOT NULL, listeria_bacterium_level INT NOT NULL);")

cursor.close()
cnx.close()
