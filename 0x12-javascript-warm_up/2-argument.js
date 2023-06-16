#!/usr/bin/node

// print a message depending of the number of argument passed:
// import an anonymous module

const prog = process.argv.length;

if (prog === 2) {
	console.log('No argument')
}
else if (prog > 2) {
	console.log('Argument found');
}
