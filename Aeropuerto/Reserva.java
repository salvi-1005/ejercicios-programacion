public class Reserva {

    private Pasajero pasajero;
    private Vuelo vuelo;
    private int asiento;

    public Reserva(Pasajero pasajero, Vuelo vuelo, int asiento){
        this.pasajero = pasajero;
        this.vuelo = vuelo;
        this.asiento = asiento;
        
    }

    public Pasajero getPasajero(){
        return pasajero;
    }

    public Vuelo getVuelo(){
        return vuelo;
    }

    public int getAsiento(){
        return asiento;
    }

    
    
}
