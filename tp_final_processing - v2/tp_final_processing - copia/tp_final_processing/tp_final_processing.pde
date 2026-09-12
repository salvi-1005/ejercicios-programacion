ModuloMB339 juego;

void setup() {
  size(600, 800);
  juego = new ModuloMB339();
  juego.inicializar();
  juego.iniciar();
}

void draw() {
  background(10, 20, 40);
  juego.actualizarCiclo();
  juego.dibujar();
}

void keyPressed() {
  juego.teclaPresionada(keyCode, key);
}

void keyReleased() {
  juego.teclaSoltada(keyCode, key);
}
