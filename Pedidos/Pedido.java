import java.util.ArrayList;

public class Pedido {

    private ArrayList<ItemPedido> lineasPedido;

    public Pedido(){
        this.lineasPedido = new ArrayList<>();
    }

    public ArrayList<ItemPedido> getLineasPedido(){
        return this.lineasPedido;
    }


    public ItemPedido agregarItem(ItemPedido item){
        lineasPedido.add(item);
        return item;
    }

    public double calcularTotalDeCompra(){
        double precioTotal = 0;
        for (ItemPedido item : lineasPedido){
            precioTotal += item.calcularPrecioTotal();
        }
        return precioTotal;
    }

    public void mostrarPedido(){
        for (ItemPedido item : lineasPedido){
            System.out.println(item.toString());
        }
    }
}
