#!/usr/bin/node
class Rectangle {
  constructor (width, height) {
    if (width > 0 && height > 0) {
      this.width = width;
      this.height = width;
    }
  }
}

module.exports = Rectangle;
