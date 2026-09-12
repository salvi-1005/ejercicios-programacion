public abstract class Viaje {
    
    protected Trayecto trayecto;
    protected int cantVagones;
    protected int capacidadPasajeros;
    protected int cantPasajeros;

    public Viaje(Trayecto trayecto, int cantVagones, int capacidadPasajeros, int cantPasajeros){
        this.trayecto = trayecto;
        this.cantVagones = cantVagones;
        this.capacidadPasajeros = capacidadPasajeros;
        this.cantPasajeros = cantPasajeros;
    }

    public abstract int tiempoDeDemora();
    
}
