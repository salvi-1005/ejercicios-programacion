public class Nave{
    private int xNave = 100;
    private int yNave = 100;
    
    Nave(int xPos, int yPos){
        this.xNave = xPos;
        this.yNave = yPos;
    }
    
    void actualizarNave(){
        this.xNave = this.xNave + 1;
    }
    
    void dibujarNave(){
        stroke(0);
        fill(0,0,255);
        rect(xNave,yNave,200,50);
        fill(255,0,0);
        rect(xNave-10, yNave-10, 15, 10);
        rect(xNave+10, yNave-10, 15, 10);
        rect(xNave-30, yNave-10, 15, 10);
        rect(xNave+30, yNave-10, 15, 10);
        rect(xNave-50, yNave-10, 15, 10);
        rect(xNave+50, yNave-10, 15, 10);
        rect(xNave-70, yNave-10, 15, 10);
        rect(xNave+70, yNave-10, 15, 10);
        rect(xNave-10, yNave+10, 15, 10);
        rect(xNave+10, yNave+10, 15, 10);
        rect(xNave-30, yNave+10, 15, 10);
        rect(xNave+30, yNave+10, 15, 10);
        rect(xNave-50, yNave+10, 15, 10);
        rect(xNave+50, yNave+10, 15, 10);
        rect(xNave-70, yNave+10, 15, 10);
        rect(xNave+70, yNave+10, 15, 10);
        
    }  
}
