const mysql = require('mysql');

const connection = mysql.createConnection({
  host: process.env.MYSQL_HOST,
  user: process.env.MYSQL_USER,
  password: process.env.MYSQL_PASSWORD,
  database: process.env.MYSQL_DATABASE,
});

function getRobot(id) {
  return new Promise((resolve, reject) => {
    connection.query('SELECT * FROM robots WHERE id = ?', [id], function (
      error,
      results,
      fields
    ) {
      if (error) {
        console.log(error);
        reject({ code: 500, error });
      } else {
        resolve(results);
      }
    });
  });
}

function getRobots() {
  return new Promise((resolve, reject) => {
    connection.query('SELECT * FROM robots', function (error, results, fields) {
      if (error) {
        reject({ code: 500, error });
      } else {
        resolve(results);
      }
    });
  });
}

function getRobotByUnit(unitId) {
  return new Promise((resolve, reject) => {
    connection.query('SELECT * FROM robots WHERE unit_number = ?', [unitId], function (
      error,
      results,
      fields
    ) {
      if (error) {
        console.log(error);
        reject({ code: 500, error });
      } else {
        resolve(results);
      }
    });
  });
}

module.exports = {
  getRobot,
  getRobots,
  getRobotByUnit
};
