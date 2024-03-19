#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	let a = 0;
	let i;
	for (i = 0; i < list.length; i++) {
	  a = (list[i] === searchElement) ? a + 1 : a;
	}
	return a;
};
