const express = require('express');
const router = express.Router();
const { incrementCount } = require('../visitorCounter');

router.post('/', (req, res) => {
  const count = incrementCount();
  res.json({ count });
});

module.exports = router;