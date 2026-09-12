public class Marciano{
    private int xMarciano = 300;
    private int yMarciano = 300;
    
    
    Marciano(int xPos, int yPos){
        this.xMarciano = xPos;
        this.yMarciano = yPos;
      }
    
    void actualizarMarciano(){
        this.xMarciano = this.xMarciano + 1;
    }

    void dibujarMarciano(){
        stroke(0);
        fill(0,255,0);
        ellipse(xMarciano,yMarciano,40,40);
        fill(255,255,0);
        ellipse(xMarciano-10, yMarciano-10, 15, 10);
        ellipse(xMarciano+10, yMarciano-10, 15, 10);
   
        
    }
    }
