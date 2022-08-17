#!/usr/bin/node
const fs = require('fs');
const content = process.argv[3];
const axios = require('axios').default;
axios.get(process.argv[2])
  .then(function (response) {
    fs.writeFile(content, response.data, err => {
      if (err) {
        console.log(err);
      }
    })
  });
