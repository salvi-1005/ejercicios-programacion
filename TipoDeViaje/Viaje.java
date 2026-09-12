public class Viaje {

    private Trayecto trayecto;
    private int cantPasajeros;
    private TipoDeViaje tipo;

    public Viaje(Trayecto trayecto, int cantPasajeros, TipoDeViaje tipo) {
        this.trayecto = trayecto;
        this.cantPasajeros = cantPasajeros;
        this.tipo = tipo;
    }

    public int tiempoDeDemora() {
        return tipo.tiempoDeDemora(trayecto, cantPasajeros);
    }
}
