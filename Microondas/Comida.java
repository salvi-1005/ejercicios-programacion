public class Comida {

    private String nombre;
    private int puntos;

    public Comida(String nombre, int puntos){
        this.nombre = nombre;
        this.puntos = puntos;
    }
    
    public String getNombre(){
        return nombre;
    }
    
    public int getPuntos(){
        return puntos;
    }
    
    public void sumarPuntos(int puntos) {
        this.puntos += puntos;
    }

    public String toString() {
        return nombre + " (" + puntos + " pts)";
    }

}
