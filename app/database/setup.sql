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

CREATE USER 'admin_delegate'@'localhost' IDENTIFIED BY 'admin_delegate';
GRANT CREATE, DROP, GRANT OPTION, INSERT, SELECT, UPDATE, DELETE ON  devops. * TO 'admin_delegate'@'localhost';

CREATE USER 'concentrateur_docker'@'localhost' IDENTIFIED BY 'concentrateur_docker';
GRANT INSERT, SELECT on devops.robots TO 'concentrateur_docker'@'localhost';

CREATE USER 'data_vision'@'localhost' IDENTIFIED BY 'data_vision';
GRANT SELECT on devops.robots TO 'data_vision'@'localhost';

FLUSH PRIVILEGES;
