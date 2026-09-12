public class AltaVelocidad extends TipoDeViaje {

    @Override
    public int tiempoDeDemora(Trayecto trayecto, int cantPasajeros) {
        int dist = trayecto.getDistancia();
        return dist / 10;
    }
}
