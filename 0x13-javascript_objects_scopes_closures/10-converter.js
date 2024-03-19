#!/usr/bin/node
//converts a number from base 10 to another

exports.converter = function (base) {
  return function (r) {
    return r.toString(base);
  };
};
