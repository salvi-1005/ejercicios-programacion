public class Monedero {
    private int cantidadDinero;

    public Monedero(int cantidadDinero){
        this.cantidadDinero = cantidadDinero;
    }

    public void MeterDinero(int dinero){
        this.cantidadDinero += dinero;
    }

    public void SacarDinero(int dinero){
        if (this.cantidadDinero >= dinero){
            this.cantidadDinero -= dinero;
        }
        
        //Si quiero sacar más dinero del que tengo disponible, entonces saco todo lo que tengo 
        // y quedo en cero.
        else{
            System.out.println("No hay suficiente dinero");
        }
    }
    
    public int ConsultarDineroDisponible(){
        return this.cantidadDinero;
    }

}
