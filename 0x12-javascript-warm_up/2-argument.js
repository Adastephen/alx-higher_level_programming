#!/usr/bin/node

// print a message depending of the number of argument passed:
// import an anonymous module
const process = require('process');

if (process.argv === null) {
	console.log('No argument');
}
else {
	console.log('Argument found');
}
