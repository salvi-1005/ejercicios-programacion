public class SucesionEstadistica {
    
    private double[] datos;
    private int cantidad; //Cantidad de elementos en la lista hasta el momento

    public SucesionEstadistica(int cota) {
        if(cota <= 0) {
            throw new IllegalArgumentException("Capacidad invalida");
        }
        this.datos = new double[cota];
        this.cantidad = 0;
    }

    public void agregarDato(double dato) {
        if (cantidad < datos.length) {
            datos[cantidad] = dato;
            cantidad++;
        } else {
            System.out.println("No se pueden agregar más datos, la sucesión está llena.");
        }
    }

    public int getCantidad() {
        return cantidad;
    }

    public double calcularMedia() {
        if (cantidad == 0) {
            System.out.println("No se han agregado datos para calcular la media.");
            return 0;
        }
        double suma = 0;
        for (int i = 0; i < cantidad; i++) {
            suma += datos[i];
        }
        return suma / cantidad;
    }

    public double calcularDesviacionEstandar() {
        if (cantidad == 0) {
            System.out.println("No se han agregado datos para calcular la desviación estándar.");
            return 0;
        }
        double media = calcularMedia();
        double sumaCuadrados = 0;
        for (int i = 0; i < cantidad; i++) {
            sumaCuadrados += Math.pow(datos[i] - media, 2);
        }
        return Math.sqrt(sumaCuadrados / cantidad);
    }

}
