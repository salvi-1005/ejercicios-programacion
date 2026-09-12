int x = 0;
int posX = 100;
int posY = 100;
AVQ avioncito;

void setup()
{
size(600,600);
background(0);
rectMode(CENTER);
ellipseMode(CENTER);
avioncito = new AVQ();
}

void draw()
{
fill(255,0,0);
rect(x,300,50,100);
x = x+1;
avioncito.dibujarAVQ(posX, posY);
}
