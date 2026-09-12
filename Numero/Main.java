public class Main {
    public static void main(String[] args) {

        Numero n1 = new Complejo(2, 3);
        Numero n2 = new Complejo(1, 4);

        Numero resultado = n1.sumar(n2);

        resultado.mostrar();

        Numero n3 = new Fraccion(2, 3);
        Numero n4 = new Fraccion(1, 4);

        Numero resultado2 = n3.sumar(n4);

        resultado2.mostrar();

        Numero n5 = new Vector(new double[]{2, 3});
        Numero n6 = new Vector(new double[]{1, 4});

        Numero resultado3 = n5.sumar(n6);

        resultado3.mostrar();

        Numero n7 = new Matriz(new double[][]{{6, 5},{9, 3}});
        Numero n8 = new Matriz(new double[][]{{7, 4},{8, 1}});

        Numero resultado4 = n7.sumar(n8);

        resultado4.mostrar();
    }
}