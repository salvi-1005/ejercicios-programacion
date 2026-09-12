public class Electrico extends Viaje {

    public Electrico(Trayecto trayecto, int cantVagones, int capacidadPasajeros, int cantPasajeros){
        super(trayecto, cantVagones, capacidadPasajeros, cantPasajeros);
    }

    @Override
    public int tiempoDeDemora(){
        int dist = trayecto.getDistancia();
        int cantEst = trayecto.getCantEstaciones();
        if (cantPasajeros > capacidadPasajeros) {
            throw new IllegalArgumentException("Excede la capacidad");
        }
        return (dist*cantEst/2);
    }

}
