GameManager game;

void setup()
{
  size(600, 600);
  background(0);
  game = new GameManager();
}

void draw()
{
  background(0);
  game.actualizar();
  game.dibujar();
}
