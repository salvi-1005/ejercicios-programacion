public class Bloque {
    
    private int largo;
    private int ancho;
    private int profundidad;

    public Bloque(int largo, int ancho, int profundidad) {
        this.largo = largo;
        this.ancho = ancho;
        this.profundidad = profundidad;
    }

    public int getLargo() {
        return largo;
    }

    public int getAncho() {
        return ancho;
    }

    public int getProfundidad() {
        return profundidad;
    }

}
