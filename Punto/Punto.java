public class Punto {
public int x;
public int y;
public Punto(int a, int b) {
    x = a; 
    y = b;
}
public Punto(int z) {
    this(z, z);
}

public void asignarValores(int c, int d){
    this.x = c;
    this.y = d;
}

public int coordenadaX(Punto p){
    return p.x;
}

public int coordenadaY(Punto p){
    return p.y;
}

public Punto suma(Punto p){
    int x = this.x + p.x;
    int y = this.y + p.y;
    return new Punto(x,y);
}

public boolean igualdad(Punto p1, Punto p2){
      return (p1.x == p2.x && p1.y == p2.y);

}

}
