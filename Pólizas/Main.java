import java.time.LocalDate;

public class Main {

    public static void main(String[] args) {
        
        Aseguradora aseguradora = new Aseguradora("Seguros XYZ");

        Cliente cliente1 = new Cliente("Juan", "Perez", LocalDate.of(1990, 6, 15)); // Fecha de nacimiento: 15 de junio de 1990
        
        Vehiculo vehiculo1 = new Vehiculo("ABC123", 2015, 15000);
        Vehiculo vehiculo2 = new Vehiculo("XYZ789", 2020, 30000);

        Poliza polizaVehiculo = aseguradora.asegurarVehiculo(cliente1, 20000.0, LocalDate.of(2026, 1, 1), LocalDate.of(2027, 1, 1), vehiculo1);
        Poliza polizaVida = aseguradora.asegurarVida(cliente1, 100000.0, LocalDate.of(2026, 1, 1), LocalDate.of(2027, 1, 1));
        Poliza polizaAutomotorNoVigente = aseguradora.asegurarVehiculo(cliente1, 50000.0, LocalDate.of(2024, 1, 1), LocalDate.of(2025, 1, 1), vehiculo2); // Póliza no vigente
    
        aseguradora.mostrarPolizas();

        // Transferir la póliza de automotor a otro cliente
        Cliente cliente2 = new Cliente("Maria", "Gomez", LocalDate.of(1985, 3, 20)); // Fecha de nacimiento: 20 de marzo de 1985
        aseguradora.transferirPoliza(polizaVehiculo, cliente2);

        System.out.println("\nDespues de transferir la poliza de automotor a Maria Gomez:");
        aseguradora.mostrarPolizas();

        Cliente cliente3 = new Cliente("Carlos", "Lopez", LocalDate.of(2000, 12, 5)); // Fecha de nacimiento: 5 de diciembre de 2000
        aseguradora.transferirPoliza(polizaAutomotorNoVigente, cliente3); // Intentar transferir a un nuevo cliente
        aseguradora.transferirPoliza(polizaVida, cliente3); // Intentar transferir una póliza de vida

    }
    
}
