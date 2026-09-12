import java.util.ArrayList;

public class Concesionaria {

    private ArrayList<Camion> camionesRegistrados;

    public Concesionaria() {
        camionesRegistrados = new ArrayList<>();
    }

    public boolean verificarCamion(Camion c) {
        // lógica (simulada)
        boolean cumple = true;

        if (cumple) {
            camionesRegistrados.add(c);
            return true;
        }

        return false;
    }
}
