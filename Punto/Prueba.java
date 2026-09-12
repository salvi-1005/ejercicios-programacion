public class Prueba {
public static void main(String[] args) {
Punto p1 = new Punto(25);
Punto p2 = new Punto(12);
Punto p3 = new Punto(12);
System.out.println("x = " + p1.x + " y = " + p1.y);
p1.asignarValores(4, 3);
System.out.println(p1.coordenadaX(p1));
System.out.println(p1.coordenadaY(p1));
System.out.println(p2.coordenadaX(p2));
System.out.println(p2.coordenadaY(p2));
System.out.println(p3.coordenadaX(p3));
System.out.println(p3.coordenadaY(p3));
Punto p4 = p2.suma(p1);
System.out.println(p3.coordenadaX(p4));
System.out.println(p3.coordenadaY(p4));
System.out.println(p2.igualdad(p1, p3));
System.out.println(p2.igualdad(p2, p3));
}
}