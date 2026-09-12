public class Main {
    
    public static void main(String[] args) {

        Producto producto1 = new Producto("Laptop", 1500.00, 10);
        Producto producto2 = new Producto("Smartphone", 800.00, 20);
        Producto producto3 = new Producto("Tablet", 500.00, 0);

        Inventario inventario = new Inventario();
        inventario.agregarProducto(producto1);
        inventario.agregarProducto(producto2);
        inventario.agregarProducto(producto3);

        System.out.println("Valor total del inventario: " + inventario.calcularValorTotal());
        inventario.venderProducto(producto1);
        System.out.println("Cantidad de laptops en inventario: " + producto1.getCantidad());
        System.out.println("Valor total del inventario después de vender un producto: " + inventario.calcularValorTotal());
        inventario.mostrarProductosAgotados();
        inventario.buscarProductoPorNombre("Laptop");
        inventario.buscarProductoPorNombreParcial("phone");

    }

}
