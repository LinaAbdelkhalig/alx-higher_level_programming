#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) { super.print(); } else {
      const row = 'C'.repeat(this.width);
      for (let i = 0; i < this.height; i++) { console.log(row); }
    }
  }
}

module.exports = Square;
