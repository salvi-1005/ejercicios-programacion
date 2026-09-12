import java.time.LocalDate;

public class Main {
    
    public static void main(String[] args) {
        Camion camion = new Camion(LocalDate.of(2023, 12, 1), false);
        Concesionaria concesionaria = new Concesionaria();

        camion.solicitarAutorizacion(concesionaria);
        camion.habilitar(LocalDate.of(2023, 12, 2));
        System.out.println(concesionaria.verificarCamion(camion)); // true

}
}