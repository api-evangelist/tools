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

  var organization = req.query.organization;
  var search = req.query.search;
  
  var limit = req.query.limit;
  if(limit){
    if(limit == ''){
      limit = 25;
    }
  }
  else{
    limit = 25;
  }

  var page = req.query.page;
  if(page){
    if(page == ''){
      page = 0;
    }
  }
  else{
    page = 0;
  }

  var count_sql = "SELECT count(name) as toolCount FROM tools WHERE name IS NOT NULL";
  if(search){
    count_sql += " AND (name LIKE '%" + search + "%' OR description LIKE '%" + search + "%' OR tags LIKE '%" + search + "%')";
  }
  connection.query(count_sql, function (error, total, fields) { 

    var tools_sql = "SELECT * FROM tools WHERE name IS NOT NULL";
    if(search){
      tools_sql += " AND (name LIKE '%" + search + "%' OR description LIKE '%" + search + "%' OR tags LIKE '%" + search + "%')";
    }    
    tools_sql += " LIMIT " + page + "," + limit;

    connection.query(tools_sql, function (error, tools, fields) { 

      var totalRecords = total[0].toolCount;
      var totalPages = Math.round(totalRecords/limit);

      var meta = {};
      if(search){
        meta.search = search;
      }
      meta.limit = limit;
      meta.page = page;
      meta.totalPages = totalPages;
      meta.count_sql = count_sql;
      meta.tools_sql = tools_sql;

      var response = {};
      response.meta = meta;
      response.data = tools;
      
      resp.send(response);    
      
    }).on('error', err => {
      resp.send(err);
    });         
  }).on('error', err => {
    resp.send(err);
  });                   

});


router.post('/', jsonParser, (req, resp)=>{ 

  var bucket = 'api-evangelist';  
  var organization = req.query.organization;
  var tool = req.body;   

  var check_tool_sql = "SELECT * FROM tools WHERE name = " +  connection.escape(tool.name);
  connection.query(check_tool_sql, function (error, exists, fields) {                   

    if(exists.length > 0){
      //Already Exists
      tool.message = 'Already Exists!';
      resp.send(tool);
    }
    else{

      tool.name = tool.name.trim();
      tool.description = tool.description.trim();
      tool.slug = common.slugify(tool.name);
      tool.image = 'https://example.com/images.jpg';
      tool.properties = [];
      tool.tags = ['New'];
      tool.tool = {};

      var markdown_tool = '---\r\n' + yaml.dump(tool) + '---\r\n';

      var insert_tool_sql = "INSERT INTO tools(name,description,tool) VALUES";
      insert_tool_sql += "(" + connection.escape(tool.name) + "," + connection.escape(tool.description) + "," + connection.escape(JSON.stringify(tool)) + ")";
      connection.query(insert_tool_sql, function (error, insert_results, fields) {     
              
        tool.id = insert_results.insertId;

        var github_url = 'https://api.github.com/repos/' + organization + '/tools/contents/_tools/' + common.slugify(tool.name) + '.md';     

        var c = {};
        c.name = "Kin Lane";
        c.email = "kinlane@gmail.com";

        var m = {};
        m.message = 'Writing New Rule';
        m.committer = c;
        m.content = btoa(markdown_tool);

        const options = {
          method: 'put',
          headers: {
          "Accept": "application/vnd.github+json",
          "X-GitHub-Api-Version": "2022-11-28",
          "Authorization": 'Bearer ' + github_token                
          },
          body: JSON.stringify(m)
        };                    
        
        fetch(github_url,options)
          .then(function(response) {
              if (!response.ok) {      
                
                var key = 'tools/tools/' + common.slugify(tool.name) + '.md';
                var params = {
                  Bucket : bucket,
                  Key : key,
                  Body : markdown_tool
                };

                const put_command = new PutObjectCommand(params);
          
                client.send(put_command).then(
                  (put) => {  

                    var status = response.status;  
                    var m = {};
                    m.status = status;
                    //m.github_url = github_url;                         
                    //m.options = options;    
                    //m.insert_tool_sql = insert_tool_sql;
                    m.tool = tool;    
                    resp.send(m);                      
                    
                },
                (error) => {
                  resp.send("1");
                }
                );

              }
              response.json().then(function(data) { 

                var key = 'tools/tools/' + common.slugify(tool.name) + '.md';
                var params = {
                  Bucket : bucket,
                  Key : key,
                  Body : markdown_tool
                };
          
                const put_command = new PutObjectCommand(params);
          
                client.send(put_command).then(
                  (put) => {                                                       
                    
                    var m = {};
                    //m.github_url = github_url;                         
                    //m.options = options;    
                    //m.insert_tool_sql = insert_tool_sql;
                    m.tool = tool;    
                    //m.data = data; 
                    //m.insert_results = insert_results;
                    resp.send(m);                      
                    
                },
                (error) => {
                  resp.send("2");
                }
                );

              });
            })
            .catch(function(err) {
                console.log('Error: ' + err);            
                resp.send(err);                     
          });                 

      }).on('error', err => {
        resp.send(err);
      }); 

    }      

  }).on('error', err => {
    resp.send(err);
  });  
        
});

module.exports = router;