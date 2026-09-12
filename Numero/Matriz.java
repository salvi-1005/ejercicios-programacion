public class Matriz extends Numero {

    private double[][] datos;

    public Matriz(double[][] datos) {
        this.datos = datos;
    }

    @Override
    public Numero sumar(Numero otro) {
        Matriz m = (Matriz) otro;

        int filas = datos.length;
        int cols = datos[0].length;

        double[][] res = new double[filas][cols];

        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < cols; j++) {
                res[i][j] = datos[i][j] + m.datos[i][j];
            }
        }

        return new Matriz(res);
    }

    @Override
    public Numero multiplicar(Numero otro) {
        Matriz m = (Matriz) otro;

        int filas = datos.length;
        int cols = m.datos[0].length;
        int comun = datos[0].length;

        double[][] res = new double[filas][cols];

        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < cols; j++) {
                for (int k = 0; k < comun; k++) {
                    res[i][j] += datos[i][k] * m.datos[k][j];
                }
            }
        }

        return new Matriz(res);
    }

    @Override
    public void mostrar() {
        for (double[] fila : datos) {
            for (double d : fila) {
                System.out.print(d + " ");
            }
            System.out.println();
        }
    }
}
