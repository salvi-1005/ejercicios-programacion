import java.time.LocalDate;
import java.util.ArrayList;

public class Aseguradora {

    private String nombre;
    private ArrayList<Poliza> polizas;

    public Aseguradora(String nombre) {
        this.nombre = nombre;
        this.polizas = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public Poliza asegurarVida(Cliente cliente, double montoAsegurado, LocalDate fechaInicio, LocalDate fechaFin) {
        Vida vida = new Vida(cliente, montoAsegurado, fechaInicio, fechaFin);
        polizas.add(vida);
        return vida;
    }

    public Poliza asegurarVehiculo(Cliente cliente, double montoAsegurado, LocalDate fechaInicio, LocalDate fechaFin, Vehiculo vehiculo) {
        Automotor automotor = new Automotor(cliente, montoAsegurado, fechaInicio, fechaFin, vehiculo);
        polizas.add(automotor);
        return automotor;
    }

    public void transferirPoliza(Poliza poliza, Cliente nuevoCliente) {
        if (!polizas.contains(poliza)) {
            System.out.println("La poliza no pertenece a esta aseguradora.");
            return;
        }
        if (poliza instanceof Vida) {
            System.out.println("No se pueden transferir polizas de vida.");
            return;
        }
        if (!poliza.estaVigente()) {
            System.out.println("La poliza no esta vigente. No se puede transferir.");
            return;
        }
        if (poliza.estaVigente() && poliza instanceof Automotor) {
            poliza.setCliente(nuevoCliente);
            System.out.println("Poliza transferida exitosamente a " + nuevoCliente.getNombre() + " " + nuevoCliente.getApellido());
        } 
    }

    public void mostrarPolizas() {
        System.out.println(" --- Polizas Vigentes --- ");
        for (Poliza poliza : polizas) {
            if (poliza.estaVigente()) {
                System.out.println(poliza.toString());
            }
        }
        System.out.println("\n --- Polizas No Vigentes --- ");
        for (Poliza poliza : polizas) {
            if (!poliza.estaVigente()) {
                System.out.println(poliza.toString());
            }
        }
    }
    
}
