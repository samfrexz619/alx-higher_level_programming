#!/usr/bin/node
process.argv[2] === undefined ?
	console.log('No argument') :
	console.log(process.argv[2])
