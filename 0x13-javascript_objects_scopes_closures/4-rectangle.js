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

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
