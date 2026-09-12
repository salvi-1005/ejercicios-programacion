import java.util.Date;

public class Main {
    
    public static void main(String[] args) {
        
        Cliente cliente1 = new Cliente("Ana", "López", "123456789", "ana.lopez@email.com");
        Habitacion habitacion1 = new Habitacion(101);
        Habitacion habitacion2 = new Habitacion(102);
        Habitacion habitacion3 = new Habitacion(103);
        Habitacion habitacion4 = new Habitacion(104);
        Habitacion habitacion5 = new Habitacion(105);

        
        Date entrada = new Date();
        Date salida = new Date(System.currentTimeMillis() + 86400000);

        Hotel hotel = new Hotel();

        Reserva reserva1 = hotel.reservarHabitacion(cliente1, habitacion1, entrada, salida);

        hotel.agregarHabitacion(habitacion1);
        hotel.agregarHabitacion(habitacion2);
        hotel.agregarHabitacion(habitacion3);
        hotel.agregarHabitacion(habitacion4);
        hotel.agregarHabitacion(habitacion5);
        hotel.reservarHabitacion(cliente1, habitacion1, entrada, salida);
        hotel.mostrarInformacionDeLasReservasDeUnCliente(cliente1);
        double costoTotal = hotel.calcularCostoTotalDeUnaReserva(reserva1);
        System.out.println("Costo total de la reserva: " + costoTotal);
        Date medio = new Date(System.currentTimeMillis() + 864000);
        System.out.println(hotel.estaOcupadaEnFecha(habitacion1, medio));
        hotel.cancelarReserva(cliente1, reserva1);
        hotel.mostrarInformacionDeLasReservasDeUnCliente(cliente1);
        int disponibilidad = hotel.calcularDisponibilidadDeHabitacionesEnUnaFechaEspecifica(entrada);
        System.out.println("Disponibilidad de habitaciones: " + disponibilidad);

        
        System.out.println(hotel.estaOcupadaEnFecha(habitacion1, medio));
        

    }
}
