#!/usr/bin/node

const fs = require('fs');
const argv = process.argv;

if (argv.length === 5) {
  const f1 = argv[2];
  const f2 = argv[3];
  const dest = argv[4];

  try {
    const data1 = fs.readFileSync(f1, 'utf8');
    const data2 = fs.readFileSync(f2, 'utf8');

    fs.writeFileSync(dest, data1 + data2);
  } catch (err) {
    console.error(err);
  }
}
