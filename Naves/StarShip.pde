public class StarShip extends Nave
{
  StarShip(int xPos, int yPos)
  {
    super(xPos, yPos);
  }
  
  public void actualizar()
  {
    if(keyPressed)
    {
      if(key == 'a')
      {
        if(x > 4)
        {
        this.x = this.x - 2;
        }
      }
      
      if(key == 'd')
      {
        if (x < 596)
        {
        this.x = this.x + 2;
      }
      }
    }
  }
  
  public void dibujar()
  {
    fill(0,255,255);
    rect(this.x,this.y,40,20);
  }
}
