import java.time.LocalDateTime;
import java.util.ArrayList;

public class Vuelo {

    private ArrayList<Reserva> reservas;
    private int id;
    private Pasajero[] pasajeros;
    private int asientosLibres;
    private LocalDateTime horarioSalida;
    private LocalDateTime horarioLlegada;
    private String ciudadSalida;
    private String ciudadLlegada;

    public Vuelo(int id, int asientosLibres, LocalDateTime horarioSalida, LocalDateTime horarioLlegada,  String ciudadSalida, String ciudadLlegada){
        this.reservas = new ArrayList<>();
        this.id = id;
        this.pasajeros = new Pasajero[asientosLibres];
        this.horarioSalida = horarioSalida;
        this.horarioLlegada = horarioLlegada;
        this.asientosLibres = asientosLibres;
        this.ciudadSalida = ciudadSalida;
        this.ciudadLlegada = ciudadLlegada;
    }

    public ArrayList<Reserva> getReservas(){
        return this.reservas;
    }

    public int getId(){
        return this.id;
    }

    public Pasajero[] getPasajeros(){
        return this.pasajeros;
    }

    public int getAsientosLibres(){
        return this.asientosLibres;
    }

    public void setAsientosLibres(int a){
        this.asientosLibres = a;
    }

    public LocalDateTime getHorarioSalida(){
        return this.horarioSalida;
    }

    public LocalDateTime getHorarioLlegada(){
        return this.horarioLlegada;
    }

    public String getCiudadSalida(){
        return this.ciudadSalida;
    }

    public String getCiudadLlegada(){
        return this.ciudadLlegada;
    }

    public void reservarAsiento(Pasajero p, int asiento){
        if (pasajeros[asiento] != null){
            System.out.println("El asiento " + asiento + " esta ocupado");
            return;
        }
        if (asiento >= pasajeros.length || asiento < 0){
            System.out.println("el asiento " + asiento + " no existe en el vuelo " + this.id);
            return;
        }
        pasajeros[asiento] = p;
        reservas.add(new Reserva(p, this, asiento));
        asientosLibres -= 1;
    }

    public void cancelarReserva(Reserva reserva){
        reservas.remove(reserva);
        pasajeros[reserva.getAsiento()] = null;
        asientosLibres += 1;
    }

    public String toString(){
        return (id + " " + ciudadSalida + " " + ciudadLlegada);
    }
    
}
