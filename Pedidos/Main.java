public class Main {

    public static void main(String[] args){

        Tienda tienda = new Tienda("Supermercado Dia");

        Producto serenito = tienda.agregarProducto(new Producto("Serenito", 1200));
        serenito.setStock(3);
        Producto mantecaDeMani = tienda.agregarProducto(new Producto("Manteca de mani", 1500));
        mantecaDeMani.setStock(2);
        Producto chocolateAguila = tienda.agregarProducto(new Producto("Chocolate Aguila", 4000));
        chocolateAguila.setStock(1);

        Cliente cliente1 = tienda.registrarCliente(new Cliente("Carlos", "Rodriguez",10000));
        Cliente cliente2 = tienda.registrarCliente(new Cliente("Pedro", "Martinez",10000));

        Pedido pedido1 = new Pedido();

        pedido1.agregarItem(new ItemPedido(serenito, 3));
        pedido1.agregarItem(new ItemPedido(mantecaDeMani, 1));

        cliente1.realizarPedido(pedido1, tienda);

        Pedido pedido2 = new Pedido();

        pedido2.agregarItem(new ItemPedido(mantecaDeMani, 1));
        pedido2.agregarItem(new ItemPedido(chocolateAguila, 1));

        cliente2.realizarPedido(pedido2, tienda);

        tienda.mostrarNProductosMasVendidos(2);

        tienda.mostrarClienteQueMasGasto();

        tienda.aplicarDescuento(serenito, 0.2);
        tienda.aplicarDescuento(mantecaDeMani, 0.2);

    }
    
}
