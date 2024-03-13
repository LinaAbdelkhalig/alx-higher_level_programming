#!/usr/bin/node
const fs = require('fs');

const [file1, file2, destiny] = process.argv.slice(2);
fs.readFile(file1, 'utf-8', (err, data1) => {
  if (err) throw err;

  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) throw err;

    fs.writeFile(destiny, data1 + data2, (err) => {
      if (err) throw err;
    });
  });
});
