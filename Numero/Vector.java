public class Vector extends Numero {

    private double[] datos;

    public Vector(double[] datos) {
        this.datos = datos;
    }

    @Override
    public Numero sumar(Numero otro) {
        Vector v = (Vector) otro;

        double[] resultado = new double[datos.length];

        for (int i = 0; i < datos.length; i++) {
            resultado[i] = datos[i] + v.datos[i];
        }

        return new Vector(resultado);
    }

    @Override
    public Numero multiplicar(Numero otro) {
        Vector v = (Vector) otro;

        double productoEscalar = 0;

        for (int i = 0; i < datos.length; i++) {
            productoEscalar += datos[i] * v.datos[i];
        }

        return new Complejo(productoEscalar, 0); // o Double envuelto
    }

    @Override
    public void mostrar() {
        for (double d : datos) {
            System.out.print(d + " ");
        }
        System.out.println();
    }
}
