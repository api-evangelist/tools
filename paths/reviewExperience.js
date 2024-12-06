const spectralCore = require('@stoplight/spectral-core')
const { Spectral, Document } = spectralCore
const Parsers = require('@stoplight/spectral-parsers')
const { truthy, pattern, xor } = require('@stoplight/spectral-functions')
const {
  bundleAndLoadRuleset
} = require('@stoplight/spectral-ruleset-bundler/with-loader')
const spectralRuntime = require('@stoplight/spectral-runtime')
const { fetch } = spectralRuntime
const fs = require('fs');
const path = require('path');
const { S3Client, GetObjectCommand, PutObjectCommand } = require("@aws-sdk/client-s3");
const express = require('express');
const bodyParser = require('body-parser');
const router = express.Router({ mergeParams: true });
const mysql = require('mysql');
const yaml = require('js-yaml');
const store = require('../../store/keys.json');
var github_token = store.github_token;
const common = require('../../libraries/common');
const spectral = new Spectral();

const client = new S3Client({ 
    region: "us-east-1", 
    credentials: {
        accessKeyId: store.aws_access_key,
        secretAccessKey: store.aws_secret_key
    }});

var connection = mysql.createConnection({
  host     : store.api_search_database_host,
  database : store.api_search_database_database,
  user: store.api_search_database_user,
  password: store.api_search_database_password
  });

var jsonParser = bodyParser.json()

router.put('/', jsonParser, async (req, res, next) => {

  try {

    var experienceId = req.params.experienceId;
    var organization = req.query.organization;    

    var experience = req.body; 
    var experience_yaml = yaml.dump(experience)

    var bucket = organization;
    if(organization == 'api-evangelist'){
      bucket = organization;
    }
    else{
      bucket = 'apis-io';
    }         
  
    var rules_path = '/laneworks/api-evangelist/rules/experience-rules.yml';
    var ruleset = await bundleAndLoadRuleset(rules_path, { fs, fetch });

    spectral.setRuleset(ruleset);

    return spectral.run(experience_yaml).then(results => {

      const event = new Date();
      var review = {};
      review.executed = event.toISOString();
      review.results = results;                 
      
      var key ='experiences/' + experience.slug + '-review.yml';
      var params = {
        Bucket : bucket,
        Key : key,
        Body : yaml.dump(review)
      };      

      const put_command = new PutObjectCommand(params);

      client.send(put_command).then(
        (put) => {                           
    
          // update database
          var update_experiences = "UPDATE experiences SET changes = 1,review = " + connection.escape(JSON.stringify(review)) + " WHERE id = '" + experienceId + "'";
          connection.query(update_experiences, function (error, changes, fields) {                   

            // insert change    
            var insert_changes = "INSERT INTO experience_changes(experienceId,name,description,file) VALUES (" + connection.escape(experienceId) + ",'API Review','This was an automated review of the API using relevant experienceset'," + connection.escape(key) + ")";
            connection.query(insert_changes, function (error, changes, fields) {                                                   
              
              res.send(review);                       

            }).on('error', err => {
              res.send(err);
            });  
            // End insert change

          }).on('error', err => {
            res.send(err);
          });  
          // End Update Database     

      },
      (error) => {
        res.send(error);
      }
      );                           
      // End Write Last      
      
    });  
    
  } catch (err) {
    res.send(err);
  } 

}); 

module.exports = router;