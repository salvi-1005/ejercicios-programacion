public class Electrico extends TipoDeViaje {

    @Override
    public int tiempoDeDemora(Trayecto trayecto, int cantPasajeros) {
        int dist = trayecto.getDistancia();
        int cantEst = trayecto.getCantEstaciones();
        return (dist * cantEst / 2);
    }
}
