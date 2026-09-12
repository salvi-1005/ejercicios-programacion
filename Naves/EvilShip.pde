public class EvilShip extends Nave
{
  int direction;
  
  EvilShip(int xPos, int yPos)
  {
    super(xPos, yPos);
    this.direction = 5;
  }
  
  public void actualizar()
  {
    this.x = this.x + 5;
    if(this.x == 600 || this.x == 0)
    {
      this.direction = this.direction * (-1);
    }
  }

  public void dibujar()
  {
    fill(0,255,0);
    ellipse(this.x,this.y,30,30);
  }
}
