class Martian{

  int xPos;
  int yPos;
  int dirMartian;
  
  Martian(int x, int y)
  {
    xPos = x;
    yPos = y;
    dirMartian = 1;
  }
  
  void actualizarMarcianos()
  {
    xPos = xPos + dirMartian;
    if(xPos == 0 || xPos == width){
      dirMartian = dirMartian *(-1);
    }
  }

  void dibujarMarcianos()
  {
    fill(0, 255, 0);
    ellipseMode(CENTER);
    ellipse(xPos, yPos, 40, 40);
  }

}
