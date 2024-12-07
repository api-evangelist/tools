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

  var toolId = req.params.toolId;
  var organization = req.query.organization;

  var tools_sql = "SELECT * FROM tools WHERE id = " + connection.escape(toolId) + " OR slug = " + connection.escape(toolId);
  connection.query(tools_sql, function (error, tools, fields) { 

    var totalPages = 1;

    var meta = {};
    meta.limit = 1;
    meta.page = 0;
    meta.totalPages = 1;

    var response = {};
    response.meta = meta;
    response.data = tools[0];
    response.tools_sql = tools_sql;
    response.params = req.params;
    response.error = error;
    
    resp.send(response);    
    
  }).on('error', err => {
    resp.send(err);
  });                         

})

router.put('/', jsonParser, (req, resp)=>{ 

  var toolId = req.params.toolId;
  var organization = req.query.organization;  

  var change_name = req.params.name;
  var change_description = req.params.description;  

  var bucket =  'api-evangelist';

  var tool = req.body;   
  var file = 'store/' + tool.name.toLowerCase() + '.md';
  var key = 'tools/' + file;
  const params = {
    Bucket: bucket,
    Key: key,
    Body : yaml.dump(tool)
  };

  const put_command = new PutObjectCommand(params);

  client.send(put_command).then(
    (put) => {        
      
      if(tool.tags){
        var tools_tags = tool.tags.join(',');
      }
      else{
        var tools_tags = '';
      }    
      
      if(tool.properties && tool.properties.length > 1){
        var tools_properties = tool.properties.join(',');
      }
      else{
        var tools_properties = '';
      }         

      var update_tool_sql = "UPDATE tools SET ";
      update_tool_sql += "name = " + connection.escape(tool.name) + ", ";
      update_tool_sql += "description = " + connection.escape(tool.description) + ", ";
      update_tool_sql += "slug = " + connection.escape(tool.slug) + ", ";
      update_tool_sql += "properties = " + connection.escape(tools_properties) + ", ";
      update_tool_sql += "image = " + connection.escape(tool.image) + ", ";
      update_tool_sql += "tags = " + connection.escape(tools_tags) + ", ";
      update_tool_sql += "tool = " + connection.escape(JSON.stringify(tool)) + " ";
      update_tool_sql += "  WHERE slug = " + connection.escape(toolId);
      
      connection.query(update_tool_sql, function (error, changes, fields) {                   

        // insert change    
        var insert_changes = "INSERT INTO tool_changes(toolId,name,description,file) VALUES (" + connection.escape(toolId) + "," + connection.escape(change_name) + "," + connection.escape(change_description) + "," + connection.escape(file) + ")";
        connection.query(insert_changes, function (error, changes, fields) {                                                   

          var response = {};
          response.update_tool_sql = update_tool_sql;
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