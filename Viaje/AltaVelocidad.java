public class AltaVelocidad extends Viaje {

    public AltaVelocidad(Trayecto trayecto, int cantVagones, int capacidadPasajeros, int cantPasajeros){
        super(trayecto, cantVagones, capacidadPasajeros, cantPasajeros);
        
    }

    @Override
    public int tiempoDeDemora(){
        int dist = trayecto.getDistancia();
        if (cantPasajeros > capacidadPasajeros) {
            throw new IllegalArgumentException("Excede la capacidad");
        }
        return dist/10;
    }

}
