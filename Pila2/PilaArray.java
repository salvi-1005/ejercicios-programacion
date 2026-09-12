import java.util.Arrays;

public class PilaArray implements Pila2 {

    private int[] datos;
    private int tope;
    private int incremento;

    public PilaArray(int capacidadInicial, int incremento) {
        this.datos = new int[capacidadInicial];
        this.tope = 0;
        this.incremento = incremento;
    }

    @Override
    public void apilar(int elemento) {
        // Si está lleno → agrandar
        if (tope == datos.length) {
            agrandarArray();
        }

        datos[tope] = elemento;
        tope++;
    }

    @Override
    public int desapilar() {
        if (estaVacia()) {
            throw new RuntimeException("Pila vacía");
        }

        tope--;
        return datos[tope]; // LIFO
    }

    @Override
    public boolean estaVacia() {
        return tope == 0;
    }

    private void agrandarArray() {
        int nuevoTam = datos.length + incremento;
        datos = Arrays.copyOf(datos, nuevoTam);
    }
}
