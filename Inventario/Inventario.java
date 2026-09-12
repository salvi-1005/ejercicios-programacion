import java.util.ArrayList;

public class Inventario {

    private ArrayList<Producto> productos;

    public Inventario() {
        this.productos = new ArrayList<>();
    }

    
    public void agregarProducto(Producto producto) {
        for (Producto p : productos) {
            if (p.getNombre().equalsIgnoreCase(producto.getNombre())) {
                p.setCantidad(p.getCantidad() + producto.getCantidad());
                return;
            }
        }
        productos.add(producto);
    }


    public void venderProducto(Producto producto) {
        if (producto.getCantidad() == 0) {
            System.out.println("Producto agotado");
            return;
        }
        
        producto.setCantidad(producto.getCantidad() - 1);
    }

    public double calcularValorTotal() {
        double valorTotal = 0;
        for (Producto producto : productos) {
            valorTotal += producto.getPrecio() * producto.getCantidad();
        }
        return valorTotal;
    }

    public void mostrarProductosAgotados() {
        ArrayList<Producto> productosAgotados = new ArrayList<>();
        System.out.println("Productos agotados:");
        for (Producto producto : productos) {
            if (producto.getCantidad() == 0) {
                productosAgotados.add(producto);
            }
        }
        for (Producto producto : productosAgotados) {
            System.out.println(producto.getNombre());
        }
    }

    public void buscarProductoPorNombre(String nombre) {
        for (Producto producto : productos) {
            if (producto.getNombre().equalsIgnoreCase(nombre)) {
                System.out.println("Producto encontrado: " + producto.getNombre() + " - Precio: " + producto.getPrecio() + " - Cantidad: " + producto.getCantidad());
                return;
            }
        }
        System.out.println("Producto no encontrado");
    }

    public void buscarProductoPorNombreParcial(String nombreParcial) {
        boolean encontrado = false;
        System.out.println("Productos encontrados con '" + nombreParcial + "':");
        for (Producto producto : productos) {
            if (producto.getNombre().toLowerCase().contains(nombreParcial.toLowerCase())) {
                System.out.println(producto.getNombre() + " - Precio: " + producto.getPrecio() + " - Cantidad: " + producto.getCantidad());
                encontrado = true;
            }
        }
        if (!encontrado) {
            System.out.println("Producto no encontrado");
        }
    }
}
