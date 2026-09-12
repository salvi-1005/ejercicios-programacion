class Rectangle {
  float x, y, w, h;

  Rectangle(float x, float y, float w, float h) {
    this.x = x;
    this.y = y;
    this.w = w;
    this.h = h;
  }

  boolean intersecta(Rectangle otro) {
    return x < otro.x + otro.w &&
           x + w > otro.x &&
           y < otro.y + otro.h &&
           y + h > otro.y;
  }
}
