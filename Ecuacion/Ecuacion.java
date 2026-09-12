public class Ecuacion {

    private double a;
    private double b;
    private double c;

    public Ecuacion(double a, double b, double c){
        this.a = a;
        this.b = b;
        this.c = c;
    }

    
    public double getA() { 
        return a; 
    }
    public double getB() { 
        return b; 
    }
    public double getC() { 
        return c; 
    }

    public double discriminante() {
        return b * b - 4 * a * c;
    }


    
    public double[] calcularRaices() {
        if (a == 0) {
            // Manejo de caso degenerado: bx + c = 0
            if (b == 0) {
                return new double[0]; // 0 = c -> o sin solución o infinitas, según c
            }
            return new double[] { -c / b };
        }

        double d = discriminante();
        if (d > 0) {
            double sqrtD = Math.sqrt(d);
            double x1 = (-b + sqrtD) / (2 * a);
            double x2 = (-b - sqrtD) / (2 * a);
            return new double[] { x1, x2 };
        } else if (d == 0) {
            double x = (-b) / (2 * a);
            return new double[] { x };
        } else {
            // No hay raíces reales
            return new double[0];
        }
    }

    
    public void imprimirRaices() {
        double[] r = calcularRaices();
        if (r.length == 2) {
            System.out.printf("Raíces reales: x1 = %.6f, x2 = %.6f%n", r[0], r[1]);
        } else if (r.length == 1) {
            System.out.printf("Raíz real doble: x = %.6f%n", r[0]);
        } else {
            System.out.println("No hay raíces reales (discriminante < 0).");
        }
    }


}
