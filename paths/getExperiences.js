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

  var count_sql = "SELECT count(name) as experienceCount FROM experiences WHERE name IS NOT NULL";
  if(search){
    count_sql += " AND (name LIKE '%" + search + "%' OR description LIKE '%" + search + "%' OR tags LIKE '%" + search + "%')";
  }
  connection.query(count_sql, function (error, total, fields) { 

    var experiences_sql = "SELECT * FROM experiences WHERE name IS NOT NULL";
    if(search){
      experiences_sql += " AND (name LIKE '%" + search + "%' OR description LIKE '%" + search + "%' OR tags LIKE '%" + search + "%')";
    }    
    experiences_sql += " LIMIT " + page + "," + limit;

    connection.query(experiences_sql, function (error, experiences, fields) { 

      var totalRecords = total[0].experienceCount;
      var totalPages = Math.round(totalRecords/limit);

      var meta = {};
      if(search){
        meta.search = search;
      }
      meta.limit = limit;
      meta.page = page;
      meta.totalPages = totalPages;
      meta.count_sql = count_sql;
      meta.experiences_sql = experiences_sql;

      var response = {};
      response.meta = meta;
      response.data = experiences;
      
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
  var experience = req.body;   

  var check_experience_sql = "SELECT * FROM experiences WHERE name = " +  connection.escape(experience.name);
  connection.query(check_experience_sql, function (error, exists, fields) {                   

    if(exists.length > 0){
      //Already Exists
      experience.message = 'Already Exists!';
      resp.send(experience);
    }
    else{

      experience.name = experience.name.trim();
      experience.description = experience.description.trim();
      experience.slug = common.slugify(experience.name);
      experience.image = 'https://example.com/images.jpg';
      experience.properties = [];
      experience.tags = ['New'];
      experience.experience = {};

      var markdown_experience = '---\r\n' + yaml.dump(experience) + '---\r\n';

      var insert_experience_sql = "INSERT INTO experiences(name,description,experience) VALUES";
      insert_experience_sql += "(" + connection.escape(experience.name) + "," + connection.escape(experience.description) + "," + connection.escape(JSON.stringify(experience)) + ")";
      connection.query(insert_experience_sql, function (error, insert_results, fields) {     
              
        experience.id = insert_results.insertId;

        var github_url = 'https://api.github.com/repos/' + organization + '/experiences/contents/_experiences/' + common.slugify(experience.name) + '.md';     

        var c = {};
        c.name = "Kin Lane";
        c.email = "kinlane@gmail.com";

        var m = {};
        m.message = 'Writing New Rule';
        m.committer = c;
        m.content = btoa(markdown_experience);

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
                
                var key = 'experiences/experiences/' + common.slugify(experience.name) + '.md';
                var params = {
                  Bucket : bucket,
                  Key : key,
                  Body : markdown_experience
                };

                const put_command = new PutObjectCommand(params);
          
                client.send(put_command).then(
                  (put) => {  

                    var status = response.status;  
                    var m = {};
                    m.status = status;
                    //m.github_url = github_url;                         
                    //m.options = options;    
                    //m.insert_experience_sql = insert_experience_sql;
                    m.experience = experience;    
                    resp.send(m);                      
                    
                },
                (error) => {
                  resp.send("1");
                }
                );

              }
              response.json().then(function(data) { 

                var key = 'experiences/experiences/' + common.slugify(experience.name) + '.md';
                var params = {
                  Bucket : bucket,
                  Key : key,
                  Body : markdown_experience
                };
          
                const put_command = new PutObjectCommand(params);
          
                client.send(put_command).then(
                  (put) => {                                                       
                    
                    var m = {};
                    //m.github_url = github_url;                         
                    //m.options = options;    
                    //m.insert_experience_sql = insert_experience_sql;
                    m.experience = experience;    
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