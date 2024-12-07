const express = require('express');
var cors = require('cors');
const app = express();

app.use(cors());

const getTools = require('./paths/getTools.js');
app.use('/tools', getTools);

const pullTools = require('./paths/pullTools.js');
app.use('/tools/pull', pullTools);

const processTools = require('./paths/processTools.js');
app.use('/tools/process', processTools);

const getTool = require('./paths/getTool.js');
app.use('/tools/:toolId', getTool);

const commitTool = require('./paths/commitTool.js');
app.use('/tools/:toolId/commit', commitTool);

const reviewTool = require('./paths/reviewTool.js');
app.use('/tools/:toolId/review', reviewTool);

app.listen(5900, () => {
  console.log('Server listening on port 5900');
});

