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

  var tools_path = '/laneworks/api-evangelist/config/tools-processing.json';
  var tools_file = fs.readFileSync(tools_path, 'utf8');
  var process_tools = JSON.parse(tools_file);  
  var processed_one = 0;
  for (let i = 0; i < process_tools.length; i++) {
    if(process_tools[i].processed == 0 && processed_one == 0){

      processed_one = 1;

      var local_tools_path = '/laneworks/api-evangelist/tools/_store/' + process_tools[i].path + '.md';
      var tools_markdown = fs.readFileSync(local_tools_path, 'utf8');
      var tools_array = tools_markdown.split("---");
      var tools_yaml = tools_array[1];
      var tool = yaml.load(tools_yaml); 

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

      var tools_sql = "INSERT INTO tools(name,description,slug,image,properties,tags,tool) VALUES";
      tools_sql += "(" + connection.escape(tool.name) + "," + connection.escape(tool.description) + "," + connection.escape(tool.slug) + "," + connection.escape(tool.image) + "," + connection.escape(tools_properties) + "," + connection.escape(tools_tags) + "," + connection.escape(JSON.stringify(tool)) + ")";
      connection.query(tools_sql, function (error, results, fields) {
            
        process_tools[i].processed = 1;
        var this_config = JSON.stringify(process_tools);
        fs.writeFileSync(tools_path, this_config, (err) => {});          

        var m = {};
        m.path = process_tools[i].path;
        m.tools_sql = tools_sql;
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