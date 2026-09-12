public class Vector3D {
public int x;
public int y;
public int z;

public Vector3D(int a, int b, int c) {
    x = a; 
    y = b;
    z = c;
}

public void asignarValores(int d, int e, int f){
    this.x = d;
    this.y = e;
    this.z = f;
}

public int coordenadaX(Vector3D v){
    return v.x;
}

public int coordenadaY(Vector3D v){
    return v.y;
}

public int coordenadaZ(Vector3D v){
    return v.z;
}

public Vector3D suma(Vector3D v){
    int x = this.x + v.x;
    int y = this.y + v.y;
    int z = this.z + v.z;
    return new Vector3D(x,y,z);
}

public boolean igualdad(Vector3D v1, Vector3D v2){
      return (v1.x == v2.x && v1.y == v2.y && v1.z == v2.z);

}

}