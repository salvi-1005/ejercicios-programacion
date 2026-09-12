import java.util.ArrayList;

public class Aeropuerto {

    private String nombre;
    private ArrayList<Vuelo> vuelos;

    public Aeropuerto(String nombre){
        this.nombre = nombre;
        this.vuelos = new ArrayList<>();
    }

    public String getNombre(){
        return this.nombre;
    }

    public void registrarVuelo(Vuelo vuelo){
        if(vuelos.contains(vuelo)){
            System.out.println("El vuelo " + vuelo.getId() + " ya está registrado en el aeropuerto " + this.nombre);
            return;
        }
        vuelos.add(vuelo);
    }

    public void verPasajerosDeUnVuelo(Vuelo vuelo){
        System.out.println("Pasajeros del avion " + vuelo.getId() + ":");
        if(!vuelos.contains(vuelo)){
            System.out.println("El vuelo " + vuelo.getId() + " no está registrado en el aeropuerto " + this.nombre);
            return;
        }
        for (Pasajero pasajero : vuelo.getPasajeros()){
            if (pasajero != null){
                System.out.println(pasajero.toString());
            }
        }
    }

    public void buscarVuelosPorDestino(String destino){
        System.out.println("Vuelos con llegada a " + destino + ":");
        for (Vuelo vuelo : vuelos){
            if (vuelo.getCiudadLlegada().equals(destino)){
                System.out.println(vuelo.toString());
            }
        }
    }

    public void mostrarVuelosCompletos(){
        System.out.println("Vuelos completos: ");
        for (Vuelo vuelo : vuelos){
            if (vuelo.getAsientosLibres() <= 0){
                System.out.println(vuelo.toString());
            }
        }
    }
    
}
