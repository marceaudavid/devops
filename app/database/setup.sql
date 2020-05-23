CREATE TABLE units (
    id INT AUTO_INCREMENT PRIMARY KEY,
    robot_number INT
);

CREATE TABLE robots (
    id INT AUTO_INCREMENT PRIMARY KEY,
    unit_number INT NOT NULL,
    robot_number INT NOT NULL,
    robot_type VARCHAR(12) NOT NULL,
    tank_temperature INT NOT NULL,
    external_temperature INT NOT NULL,
    weight_of_milk_in_tank INT NOT NULL,
    ph_measure INT NOT NULL,
    k_measure INT NOT NULL,
    nacl_concentration INT NOT NULL,
    salmonella_bacterium_level INT NOT NULL,
    e_coli_bacterium_level INT NOT NULL,
    listeria_bacterium_level INT NOT NULL,
    creation_time DATETIME NOT NULL,
    insertion_time DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE USER 'delegate'@'localhost' IDENTIFIED BY 'delegate';
GRANT CREATE, DROP, GRANT OPTION, INSERT, SELECT, UPDATE, DELETE ON * . * TO 'delegate'@'localhost';
