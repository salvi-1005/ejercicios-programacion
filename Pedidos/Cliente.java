import java.util.ArrayList;

public class Cliente {

    private String nombre;
    private String apellido;
    private double saldo;
    private ArrayList<Pedido> pedidos;
    private double plataGastada;

    public Cliente(String nombre, String apellido, double saldo){
        this.nombre = nombre;
        this.apellido = apellido;
        this.saldo = saldo;
        this.pedidos = new ArrayList<>();
        this.plataGastada = 0;
    }
    public String getNombre(){
        return this.nombre;
    }

    public String getApellido(){
        return this.apellido;
    }

    public double getSaldo(){
        return this.saldo;
    }

    public double getPlataGastada(){
        return this.plataGastada;
    }

    public void realizarPedido(Pedido pedido, Tienda tienda){
        if (pedido.calcularTotalDeCompra() > this.saldo){
            System.out.println("Saldo insuficiente");
            return;
        }
        if (!tienda.getClientes().contains(this)){
            System.out.println("El cliente " + toString() + " no está registrado en " + tienda.getNombre());
        }
        for (ItemPedido item : pedido.getLineasPedido()){
            if (item.getProducto().getStock() < item.getCantidad()){
                System.out.println("No hay suficiente stock de " + item.getProducto().getNombre());
            } else {
                item.getProducto().setStock(item.getProducto().getStock() - item.getCantidad());
                item.getProducto().setCantidadVendido(item.getProducto().getCantidadVendido() + item.getCantidad());
            }
            
        }
        pedidos.add(pedido);
        saldo -= pedido.calcularTotalDeCompra();
        plataGastada += pedido.calcularTotalDeCompra();
    }

    public String toString(){
        return (nombre + " " + apellido);
    }
    
}
