const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const mysql = require('mysql');
const yaml = require('js-yaml');
const router = express.Router();
const store = require('../../store/keys.json');
var fs = require('fs');
var path = require('path');
var github_token = store.github_token;
const common = require('../../libraries/common');

var connection = mysql.createConnection({
  host     : store.api_search_database_host,
  database : store.api_search_database_database,
  user: store.api_search_database_user,
  password: store.api_search_database_password
  });

const client = new S3Client({ 
  region: "us-east-1", 
  credentials: {
      accessKeyId: store.aws_access_key,
      secretAccessKey: store.aws_secret_key
  }});

router.get('/', (req, resp)=>{ 

  var experiences_path = '/laneworks/api-evangelist/config/experiences-processing.json';
  var experiences_file = fs.readFileSync(experiences_path, 'utf8');
  var process_experiences = JSON.parse(experiences_file);  
  var processed_one = 0;
  for (let i = 0; i < process_experiences.length; i++) {
    if(process_experiences[i].processed == 0 && processed_one == 0){

      processed_one = 1;

      var local_experiences_path = '/laneworks/api-evangelist/experiences/_store/' + process_experiences[i].path + '.md';
      var experiences_markdown = fs.readFileSync(local_experiences_path, 'utf8');
      var experiences_array = experiences_markdown.split("---");
      var experiences_yaml = experiences_array[1];
      var experience = yaml.load(experiences_yaml); 

      if(experience.tags){
        var experiences_tags = experience.tags.join(',');
      }
      else{
        var experiences_tags = '';
      }    
      
      if(experience.properties && experience.properties.length > 1){
        var experiences_properties = experience.properties.join(',');
      }
      else{
        var experiences_properties = '';
      }      

      var experiences_sql = "INSERT INTO experiences(name,description,slug,image,properties,tags,experience) VALUES";
      experiences_sql += "(" + connection.escape(experience.name) + "," + connection.escape(experience.description) + "," + connection.escape(experience.slug) + "," + connection.escape(experience.image) + "," + connection.escape(experiences_properties) + "," + connection.escape(experiences_tags) + "," + connection.escape(JSON.stringify(experience)) + ")";
      connection.query(experiences_sql, function (error, results, fields) {
            
        process_experiences[i].processed = 1;
        var this_config = JSON.stringify(process_experiences);
        fs.writeFileSync(experiences_path, this_config, (err) => {});          

        var m = {};
        m.path = process_experiences[i].path;
        m.experiences_sql = experiences_sql;
        m.config_count = i;
        m.results = results;
        resp.send(m);             
        
      }).on('error', err => {
        resp.send(err);
      });

    }
    
  }  
  if(processed_one == 0){
    var m = {};
    m.message = 'DONE';
    resp.send(m);
  }

})

module.exports = router;