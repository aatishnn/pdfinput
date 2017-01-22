const fields = require('./').read(require('fs').readFileSync('./test.pdf'))
console.log(fields)
