public class Main {
public static void main(String[] args) {
Vector3D v1 = new Vector3D(23,24,25);
Vector3D v2 = new Vector3D(10,11,12);
Vector3D v3 = new Vector3D(10,11,12);
System.out.println("x = " + v1.x + " y = " + v1.y + " z = " + v1.z);
v1.asignarValores(4, 3, 2);
System.out.println(v1.coordenadaX(v1));
System.out.println(v1.coordenadaY(v1));
System.out.println(v1.coordenadaZ(v1));
System.out.println(v2.coordenadaX(v2));
System.out.println(v2.coordenadaY(v2));
System.out.println(v2.coordenadaZ(v2));
System.out.println(v3.coordenadaX(v3));
System.out.println(v3.coordenadaY(v3));
System.out.println(v3.coordenadaZ(v3));
Vector3D v4 = v2.suma(v1);
System.out.println(v3.coordenadaX(v4));
System.out.println(v3.coordenadaY(v4));
System.out.println(v3.coordenadaZ(v4));
System.out.println(v2.igualdad(v1, v3));
System.out.println(v2.igualdad(v2, v3));
}
}