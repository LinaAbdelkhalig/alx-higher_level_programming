#!/usr/bin/node
const squareSize = process.argv[2];
if (parseInt(squareSize)) {
  let i;
  const row = 'X'.repeat(squareSize);
  for (i = 0; i < squareSize; i++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
