import java.util.ArrayList;
import java.util.Random;

public class Main {
    
    public static void main(String[] args){

        ArrayList<Medible> lista = new ArrayList<>();

        lista.add(new Termometro(20));
        lista.add(new CuentaBancaria());
        lista.add(new MedidorDePresion());

        Random rand = new Random();
        
        for (Medible m : lista) {

            System.out.println("\n--- Nuevo Medible ---");

            for (int i = 1; i <= 100; i++) {

                float valor = rand.nextInt(50) + 1; // entre 1 y 50

                // 50% incrementar, 50% decrementar
                if (rand.nextBoolean()) {
                    m.incrementar(valor);
                } else {
                    try {
                        m.decrementar(valor);
                    } catch (Exception e) {
                        System.out.println("Error en decremento: " + e.getMessage());
                    }
                }

                // Cada 10 operaciones
                if (i % 10 == 0) {
                    System.out.println("Operación " + i + 
                        " → Medida actual: " + m.obtenerMedida());
                }
            }
    }

}
}
