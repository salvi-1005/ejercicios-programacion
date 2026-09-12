import java.util.Date;

public class Reserva {

    public Date fechaEntrada;
    public Date fechaSalida;
    public Habitacion habitacion;
    public boolean reservada;
    public double costoPorNoche;

    public Reserva(Date fechaEntrada, Date fechaSalida, Habitacion habitacion, double costoPorNoche) {
        this.fechaEntrada = fechaEntrada;
        this.fechaSalida = fechaSalida;
        this.habitacion = habitacion;
        this.costoPorNoche = costoPorNoche;
        this.reservada = false;
    }


    public Date getFechaEntrada() {
        return fechaEntrada;
    }

    public Date getFechaSalida() {
        return fechaSalida;
    }


    public Habitacion getHabitacion() {
        return habitacion;
    }

    public void realizarReserva(Date fechaEntrada, Date fechaSalida) {
        this.fechaEntrada = fechaEntrada;
        this.fechaSalida = fechaSalida;
        this.reservada = true;
    }
    
    public void cancelarReserva() {
        reservada = false;
        habitacion.setCliente(null);
    }

    public double calcularCostoTotal() {
        long dias = (fechaSalida.getTime() - fechaEntrada.getTime()) / (1000 * 60 * 60 * 24);
        return dias * costoPorNoche;
    }

    public double getCostoPorNoche() {
        return costoPorNoche;
    }

}
