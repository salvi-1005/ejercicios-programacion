import java.util.ArrayList;

public class Tienda {

    private String nombre;
    private ArrayList<Cliente> clientes;
    private ArrayList<Producto> productos;

    public Tienda(String nombre){
        this.nombre = nombre;
        this.clientes = new ArrayList<>();
        this.productos = new ArrayList<>();
    }

    public String getNombre(){
        return this.nombre;
    }

    public ArrayList<Cliente> getClientes(){
        return this.clientes;
    }

    public ArrayList<Producto> getProductos(){
        return this.productos;
    }

    public Cliente registrarCliente(Cliente c){
        clientes.add(c);
        return c;
    }

    public Producto agregarProducto(Producto p){
        productos.add(p);
        p.setStock(p.getStock() + 1);
        return p;
    }

    public void mostrarNProductosMasVendidos(int n){
        System.out.println("Los " + n + " productos mas vendidos son: ");
        productos.sort((p1, p2) -> Integer.compare(p2.getCantidadVendido(), p1.getCantidadVendido()));
        for (int i = 0; i < Math.min(n, productos.size()); i++){
            System.out.println("- " + (i+1) + " " + productos.get(i).getNombre() + " (" + productos.get(i).getCantidadVendido() + ")");
        }
    }

    public void mostrarClienteQueMasGasto(){
        System.out.println("El Cliente que mas gasto es: ");
        Cliente clienteQueMasGasto = null;
        for (Cliente cliente : clientes){
            if (clienteQueMasGasto == null || cliente.getPlataGastada() > clienteQueMasGasto.getPlataGastada()){
                clienteQueMasGasto = cliente;
            }
        }
        if (clienteQueMasGasto != null){
            System.out.println(clienteQueMasGasto.toString() + " $" + clienteQueMasGasto.getPlataGastada());
        } else{
            System.out.println("No hay clientes en la tienda");
        }
    }

    public void aplicarDescuento(Producto producto, double descuento){
        producto.setPrecio(producto.getPrecio() - (producto.getPrecio() * descuento));
    }

}
