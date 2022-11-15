#!/usr/bin/node
// displays code of GET request

const request = require('request');
request(process.argv[2], function (error, response) {
  console.log(error || 'code:', response && response.statusCode);
});
