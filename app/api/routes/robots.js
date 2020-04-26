const express = require('express');
const router = express.Router();

const dao = require('../db/dao');

router.get('/', (req, res) => {
  dao
    .getRobots()
    .then((robots) => res.json(robots))
    .catch((err) => res.status(err.code).json(err.error));
});

router.get('/:id', (req, res) => {
  dao
    .getRobot(req.params.id)
    .then((robot) => res.json(robot))
    .catch((err) => res.status(err.code).json(err.error));
});

module.exports = router;
