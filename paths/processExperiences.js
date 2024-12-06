const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const router = express.Router();
const store = require('../../store/keys.json');
var fs = require('fs');
var path = require('path');
const common = require('../../libraries/common');

router.get('/', (req, resp)=>{ 

  var experiences_url = "https://experiences.apievangelist.com/store.json";

  const options = {
    method: 'get'
  };  

  fetch(experiences_url,options)
    .then(function(response) {
        if (!response.ok) {
            resp.send(response.status);
        }
        response.json().then(function(data) {   

          for (let i = 0; i < data.length; i++) {
            data[i].processed = 0;
            data[i].path = data[i].path.replace("/","");
          }

          var experiences_path = '/laneworks/api-evangelist/config/experiences-processing.json';
          var this_config = JSON.stringify(data);
          fs.writeFileSync(experiences_path, this_config, (err) => {}); 

          resp.send(this_config); 

        });
      })
      .catch(function(err) {
        resp.send(err);
  });



})

module.exports = router;