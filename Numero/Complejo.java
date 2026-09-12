public class Complejo extends Numero {

    private double real;
    private double imag;

    public Complejo(double real, double imag) {
        this.real = real;
        this.imag = imag;
    }

    @Override
    public Numero sumar(Numero otro) {
        Complejo c = (Complejo) otro;
        return new Complejo(this.real + c.real, this.imag + c.imag);
    }

    @Override
    public Numero multiplicar(Numero otro) {
        Complejo c = (Complejo) otro;

        double r = this.real * c.real - this.imag * c.imag;
        double i = this.real * c.imag + this.imag * c.real;

        return new Complejo(r, i);
    }

    @Override
    public void mostrar() {
        System.out.println(real + " + " + imag + "i");
    }
}
