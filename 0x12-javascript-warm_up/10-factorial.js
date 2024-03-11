#!/usr/bin/node
function deFacto (facto) {
  if (facto === 1 || facto === 0) {
	  return 1;
  } else {
	  return facto * deFacto(facto - 1);
  }
}
const bashArg = parseInt(process.argv[2]);
if (isNaN(bashArg)) {
  console.log(1);
} else {
  console.log(deFacto(bashArg));
}
