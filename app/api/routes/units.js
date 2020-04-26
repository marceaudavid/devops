const express = require('express');
const router = express.Router();

const dao = require('../db/dao');

router.get('/:id', (req, res) => {
  dao
    .getRobotByUnit(req.params.id)
    .then((robot) => res.json(robot))
    .catch((err) => res.status(err.code).json(err.error));
});

module.exports = router;
