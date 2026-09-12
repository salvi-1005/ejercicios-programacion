public class Van extends Automovil{
    
    public Van(String fabricante, String modelo, int añoDeFabricacion, double kilometraje, int maximoDePasajeros){
        super(fabricante, modelo, añoDeFabricacion, kilometraje, maximoDePasajeros);
    }

    @Override
    public int getMaximoDePasajeros(){
        return this.maximoDePasajeros;
    }

    @Override
    public String toString() {
        return "Van: " + modelo + " - Van: " + maximoDePasajeros;
    }

}
