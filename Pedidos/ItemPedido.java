public class ItemPedido {

    private Producto producto;
    private int cantidad;

    public ItemPedido(Producto producto, int cantidad){
        this.producto = producto;
        this.cantidad = cantidad;
    }

    public Producto getProducto(){
        return this.producto;
    }

    public int getCantidad(){
        return this.cantidad;
    }

    public double calcularPrecioTotal(){
        return producto.getPrecio() * this.cantidad;
    }

    public String toString(){
        return (this.producto + " " + this.cantidad + " " + "$" + this.calcularPrecioTotal());
    }
    
}
