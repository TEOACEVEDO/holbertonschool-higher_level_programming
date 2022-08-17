#!/usr/bin/node
const axios = require('axios').default;
axios.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2])
  .then(function (response) {
    // handle success
    console.log(response.data.title);
  })
  .catch(function (error) {
    // handle error
    console.log('code :' + error.response.status);
  })
