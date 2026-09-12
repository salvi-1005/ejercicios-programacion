class RedMartian extends Martian{
  
  RedMartian(int x, int y)
  {
    super(x, y);
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
    fill(255, 0, 0);
    ellipseMode(CENTER);
    ellipse(xPos, yPos, 40, 40);
  }

}
