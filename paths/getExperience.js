const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
const store = require('../../store/keys.json');
var github_token = store.github_token;
const common = require('../../libraries/common');

var jsonParser = bodyParser.json();  

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

  var experienceId = req.params.experienceId;
  var organization = req.query.organization;

  var experiences_sql = "SELECT * FROM experiences WHERE id = " + connection.escape(experienceId) + " OR slug = " + connection.escape(experienceId);
  connection.query(experiences_sql, function (error, experiences, fields) { 

    var totalPages = 1;

    var meta = {};
    meta.limit = 1;
    meta.page = 0;
    meta.totalPages = 1;

    var response = {};
    response.meta = meta;
    response.data = experiences[0];
    response.experiences_sql = experiences_sql;
    response.params = req.params;
    response.error = error;
    
    resp.send(response);    
    
  }).on('error', err => {
    resp.send(err);
  });                         

})

router.put('/', jsonParser, (req, resp)=>{ 

  var experienceId = req.params.experienceId;
  var organization = req.query.organization;  

  var change_name = req.params.name;
  var change_description = req.params.description;  

  var bucket =  'api-evangelist';

  var experience = req.body;   
  var file = 'store/' + experience.name.toLowerCase() + '.md';
  var key = 'experiences/' + file;
  const params = {
    Bucket: bucket,
    Key: key,
    Body : yaml.dump(experience)
  };

  const put_command = new PutObjectCommand(params);

  client.send(put_command).then(
    (put) => {        
      
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

      var update_experience_sql = "UPDATE experiences SET ";
      update_experience_sql += "name = " + connection.escape(experience.name) + ", ";
      update_experience_sql += "description = " + connection.escape(experience.description) + ", ";
      update_experience_sql += "slug = " + connection.escape(experience.slug) + ", ";
      update_experience_sql += "properties = " + connection.escape(experiences_properties) + ", ";
      update_experience_sql += "image = " + connection.escape(experience.image) + ", ";
      update_experience_sql += "tags = " + connection.escape(experiences_tags) + ", ";
      update_experience_sql += "experience = " + connection.escape(JSON.stringify(experience)) + " ";
      update_experience_sql += "  WHERE slug = " + connection.escape(experienceId);
      
      connection.query(update_experience_sql, function (error, changes, fields) {                   

        // insert change    
        var insert_changes = "INSERT INTO experience_changes(experienceId,name,description,file) VALUES (" + connection.escape(experienceId) + "," + connection.escape(change_name) + "," + connection.escape(change_description) + "," + connection.escape(file) + ")";
        connection.query(insert_changes, function (error, changes, fields) {                                                   

          var response = {};
          response.update_experience_sql = update_experience_sql;
          response.insert_changes = insert_changes;
          resp.send(response);                       

        }).on('error', err => {
          resp.send(err);
        });  
        // End insert change

      }).on('error', err => {
        resp.send(err);
      });  
      // End Update Database     
   
      },
      (error) => {
        resp.send(error);
      }
    );              

});

module.exports = router;