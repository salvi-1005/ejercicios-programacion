public class Fraccion extends Numero {

    private int num;
    private int den;

    public Fraccion(int num, int den) {
        this.num = num;
        this.den = den;
    }

    @Override
    public Numero sumar(Numero otro) {
        Fraccion f = (Fraccion) otro;

        int nuevoNum = this.num * f.den + f.num * this.den;
        int nuevoDen = this.den * f.den;

        return new Fraccion(nuevoNum, nuevoDen);
    }

    @Override
    public Numero multiplicar(Numero otro) {
        Fraccion f = (Fraccion) otro;

        return new Fraccion(this.num * f.num, this.den * f.den);
    }

    @Override
    public void mostrar() {
        System.out.println(num + "/" + den);
    }
}
