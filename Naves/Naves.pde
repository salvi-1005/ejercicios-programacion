StarShip galactica;
ArrayList<EvilShip> marcianos;

void setup()
{
  size(600, 600);
  background(0);
  rectMode(CENTER);
  ellipseMode(CENTER);
  
  galactica = new StarShip(300, 500);
  
  marcianos = new ArrayList<EvilShip>();
  for(int j = 1; j < 4; j++){
  for(int i = 1; i < 6; i++)
  {
    marcianos.add(new EvilShip(i*40,j*100));
  }
}}

void draw()
{
  background(0);
  //Actualizar Nave buena
  galactica.actualizar();
  //Dibujar la Nave buena
  galactica.dibujar();
  
  for(EvilShip m: marcianos)
  {
  //Actualizar Nave invasoras extraterrestres
  m.actualizar();
  //Dibujar Nave invasoras extraterrestres
  m.dibujar();
  }
}
