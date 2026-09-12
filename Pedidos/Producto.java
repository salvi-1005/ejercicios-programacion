public class Producto {

    private String nombre;
    private int stock;
    private double precio;
    private int cantidadVendido;

    public Producto(String nombre, double precio){
        this.nombre = nombre;
        this.stock = 0;
        this.precio = precio;
        this.cantidadVendido = 0;
    }

    public String getNombre(){
        return this.nombre;
    }

    public int getStock(){
        return this.stock;
    }

    public void setStock(int s){
        this.stock = s;
    }

    public double getPrecio(){
        return this.precio;
    }

    public void setPrecio(double p){
        this.precio = p;
    }

    public int getCantidadVendido(){
        return this.cantidadVendido;
    }

    public void setCantidadVendido(int c){
        this.cantidadVendido = c;
    }
    
}
