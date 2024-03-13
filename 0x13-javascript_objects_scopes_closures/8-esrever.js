#!/usr/bin/node
exports.esrever = function (list) {
  const rv = [];
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    rv.push(list[i]);
  }
  return rv;
};
