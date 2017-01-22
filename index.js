const join = require('path').join
const pdf = require( join(__dirname, 'build/Release/pdf') )
module.exports = {
  read: pdf.readSync,
  write: pdf.writeAsync,
  //writeSync: function writeSync ( path ) { },
  //writeAsync: function writeAsync ( path, fields, params, fn ) {}
}
