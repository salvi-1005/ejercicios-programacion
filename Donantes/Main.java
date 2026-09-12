public class Main {

    public static void main(String[] args) {
        Organizacion organizacion = new Organizacion("Organización de Donantes");

        Donante donante1 = organizacion.registrarDonante("Juan", "Pérez");
        Donante donante2 = organizacion.registrarDonante("María", "Gómez");

        System.out.println(donante1);
        System.out.println(donante2);

        Donacion cargada1 = organizacion.cargarDonacion(donante1, java.time.LocalDate.of(2024, 6, 1), 100.0);
        Donacion cargada2 = organizacion.cargarDonacion(donante2, java.time.LocalDate.of(2024, 6, 2), 200.0);
        
        System.out.println(cargada1);
        System.out.println(cargada2);

        cargada1.setCobrada();
        System.out.println(cargada1);
        cargada1.setRechazada();
        System.out.println(cargada1);
        cargada1.setCobrada();
        System.out.println(cargada1);

        organizacion.mostrarDonantes();
        organizacion.mostrarDonacionesOrdenadasPorFecha();
        organizacion.mostrarResultadoALaFecha(java.time.LocalDate.of(2024, 6, 2));
        cargada2.setCobrada();
        organizacion.mostrarResultadoALaFecha(java.time.LocalDate.of(2024, 6, 2));
    }
    
}
