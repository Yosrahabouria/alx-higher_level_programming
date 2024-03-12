#!/usr/bin/node
// class defines a rectangle

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let a;
    let b = '';
    for (a = 0; a < this.width; a++) {
      b += 'X';
    }
    for (a = 0; a < this.height; a++) {
      console.log(b);
    }
  }
}
module.exports = Rectangle;
