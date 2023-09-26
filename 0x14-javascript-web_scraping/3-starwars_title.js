#!/usr/bin/node

const req = require('request');
const epiNum = process.argv[2];
const API_URL = 'https://swapi-api.hbtn.io/api/films/';

req(API_URL + epiNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
