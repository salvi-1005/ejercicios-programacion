public class Main {
    
    public static void main(String[] args){
    
        Reporte v = new Venta("Botella", "Vino", "Rojo", "Blanco");
        v.imprimir();

        Reporte c = new Compra("Carton", "Leche");
        c.imprimir();

        Venta v2 = new Venta("Lata", "Cerveza", "Celeste","Naranja");

        v2.customizar("Verde", "Amarillo");
        v2.imprimir();
    }
}
