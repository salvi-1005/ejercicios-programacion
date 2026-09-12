public class Laboratorio extends Estudio {

    private int cantidadDeItems;

    public Laboratorio(String nombre, String descripcion, int cantidadDeItems) {
        super(nombre, descripcion);
        this.cantidadDeItems = cantidadDeItems;
    }

    public int getCantidadDeItems() {
        return cantidadDeItems;
    }

    public void realizarEstudio(Paciente p) {
        this.Estado = true;
        p.setCantEstudiosRealizados(p.getCantEstudiosRealizados() + 1);
    }

    public void mostrarResultados() {
        System.out.println("Resultados del estudio de laboratorio: " + descripcion + " (Estado: " + Estado + ")");
    }
    
}
