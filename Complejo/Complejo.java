public class Complejo {

    private double real;
    private double imaginario;

    // Constructor
    public Complejo(double real, double imaginario) {
        this.real = real;
        this.imaginario = imaginario;
    }

    // Getters
    public double getReal() {
        return real;
    }

    public double getImaginario() {
        return imaginario;
    }

    // Multiplicación
    public Complejo multiplicar(Complejo c) {
        double nuevoReal = this.real * c.real - this.imaginario * c.imaginario;
        double nuevoImaginario = this.real * c.imaginario + this.imaginario * c.real;
        return new Complejo(nuevoReal, nuevoImaginario);
    }

    // Suma de enteros
    public static int suma(int a, int b) {
        return a + b;
    }

    // Suma de floats
    public static float suma(float a, float b) {
        return a + b;
    }

    // Suma de complejos
    public Complejo suma(Complejo c) {
        double nuevoReal = this.real + c.real;
        double nuevoImaginario = this.imaginario + c.imaginario;
        return new Complejo(nuevoReal, nuevoImaginario);
    }

    // Mostrar
    @Override
    public String toString() {
        return real + " + " + imaginario + "i";
    }
}