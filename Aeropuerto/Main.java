import java.time.LocalDateTime;

public class Main {

    public static void main(String[] args){

        Aeropuerto aeropuerto = new Aeropuerto("Ezeiza");

        Vuelo vuelo1 = new Vuelo(1, 90, LocalDateTime.of(2023, 3, 8, 16, 20), LocalDateTime.of(2023, 3, 8, 20, 20), "Buenos Aires", "Lima");
        aeropuerto.registrarVuelo(vuelo1);

        Pasajero pasajero1 = new Pasajero("Salvador", "Dangelo", 44816375);
        vuelo1.reservarAsiento(pasajero1, 0);
        Pasajero pasajero2 = new Pasajero("Paula", "Fernandez", 22526104);
        vuelo1.reservarAsiento(pasajero2, 1);

        aeropuerto.verPasajerosDeUnVuelo(vuelo1);
        aeropuerto.buscarVuelosPorDestino("Lima");
        aeropuerto.mostrarVuelosCompletos();

        vuelo1.cancelarReserva(vuelo1.getReservas().get(0));

        aeropuerto.verPasajerosDeUnVuelo(vuelo1);
    }
    
}
