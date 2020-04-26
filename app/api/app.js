const express = require('express');
const cors = require('cors');
const app = express();

app.set('json spaces', 1);
app.use(cors());
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get('/', (req, res) => res.redirect('/robot'));
app.use('/robot', require('./routes/robots'));
app.use('/unit', require('./routes/units'));

app.listen(3000, () => console.log(`Running on http://localhost:${3000}`));
