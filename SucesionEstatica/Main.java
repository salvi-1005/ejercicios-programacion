public class Main {
    
    public static void main(String[] args){
        SucesionEstadistica sucesion = new SucesionEstadistica(5);
        sucesion.agregarDato(10);
        sucesion.agregarDato(20);
        System.out.println("Cantidad de datos: " + sucesion.getCantidad());
        System.out.println("Media: " + sucesion.calcularMedia());
        System.out.println("Desviacion estandar: " + sucesion.calcularDesviacionEstandar());
    }

}
