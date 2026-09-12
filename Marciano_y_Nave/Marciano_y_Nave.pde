Marciano[] m = new Marciano[10];
Nave[] n = new Nave[3];

Nave n1;
Nave n2;
Nave n3;

void setup()
{
size(600,600);
background(0);
rectMode(CENTER);
ellipseMode(CENTER);
int i = 0;
while(i<10){
  m[i] = new Marciano(i*40,100);
  i++;
}



n1 = new Nave(300,300);
n2 = new Nave(400,400);
n3 = new Nave(500,500);
}

void draw(){
  background(0);
  int i = 0;
  while(i<10){
       m[i].actualizarMarciano();
       m[i].dibujarMarciano();
       i++;
       
  }
  
  n1.actualizarNave();
  n2.actualizarNave();
  n3.actualizarNave();
  
  n1.dibujarNave();
  n2.dibujarNave();
  n3.dibujarNave();
}
