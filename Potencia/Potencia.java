public class Potencia {
    private float base;
    private int exponente;

    public Potencia(float base, int exponente) {
        this.base = base;
        this.exponente = exponente;
    }

    public float evaluar() {
        return evaluarRec(base, exponente);
    }

    // Método auxiliar recursivo
    private float evaluarRec(float b, int e) {
        // Caso base
        if (e == 0) {
            return 1;
        }
        // Caso recursivo
        return b * evaluarRec(b, e - 1);
    }
}
