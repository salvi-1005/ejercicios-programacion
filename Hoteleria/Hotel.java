import java.util.ArrayList;
import java.util.Date;

public class Hotel {

    private ArrayList<Habitacion> habitaciones;
    private ArrayList<Reserva> reservas;

    public Hotel() {
        this.habitaciones = new ArrayList<>();
        this.reservas = new ArrayList<>();
    }

    public void agregarHabitacion(Habitacion habitacion) {
        habitaciones.add(habitacion);
    }

    public Reserva reservarHabitacion(Cliente cliente, Habitacion habitacion, Date entrada, Date salida) {

        if (habitacion.getCliente() != null) {
            System.out.println("La habitación ya está ocupada");
            return null;
        }

        Reserva reserva = new Reserva(entrada, salida, habitacion, 150.0);

        reserva.realizarReserva(entrada, salida);
        reservas.add(reserva);

        habitacion.setCliente(cliente);
        cliente.asignarHabitacion(habitacion);

        return reserva; 
    }

    public void cancelarReserva(Cliente cliente, Reserva reserva) {
        Habitacion habitacion = cliente.getHabitacion();
        if (habitacion != null) {
            cliente.liberarHabitacion();
            reserva.cancelarReserva();
            reservas.remove(reserva);
        } else {
            System.out.println("El cliente no tiene una habitación reservada");
        }
    }

    public double calcularCostoTotalDeUnaReserva(Reserva reserva) {
        return reserva.calcularCostoTotal();
    }

    public int calcularDisponibilidadDeHabitacionesEnUnaFechaEspecifica(Date fecha) {
    int disponibles = 0;

    for (Habitacion habitacion : habitaciones) {
        boolean ocupadaEnFecha = false;

        for (Reserva reserva : reservas) {
            if (reserva.getHabitacion().equals(habitacion)
                && !fecha.before(reserva.getFechaEntrada())
                && !fecha.after(reserva.getFechaSalida())) {

                ocupadaEnFecha = true;
                break;
            }
        }

        if (!ocupadaEnFecha) {
            disponibles++;
        }
    }

    return disponibles;
    }

    public void mostrarInformacionDeLasReservasDeUnCliente(Cliente cliente) {
        Habitacion habitacion = cliente.getHabitacion();
        if (habitacion != null) {
            System.out.println("Cliente: " + cliente.getNombre() + " " + cliente.getApellido());
            System.out.println("Número de habitación: " + habitacion.getNumeroDeHabitacion());
        } else {
            System.out.println("El cliente no tiene una habitación reservada");
        }
    }

    public boolean estaOcupadaEnFecha(Habitacion habitacion, Date fecha) {
        for (Reserva reserva : reservas) {
            if (reserva.getHabitacion().equals(habitacion)
                && !fecha.before(reserva.getFechaEntrada())
                && !fecha.after(reserva.getFechaSalida())) {
                return true;
            }
        }
        return false;
    }
    
}
