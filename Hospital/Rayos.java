public class Rayos extends Estudio {

    private String zona;

    public Rayos(String nombre, String descripcion, String zona) {
        super(nombre, descripcion);
        this.zona = zona;
    }

    public String getZona() {
        return zona;
    }

    public void realizarEstudio(Paciente p) {
        this.Estado = true;
        p.setCantEstudiosRealizados(p.getCantEstudiosRealizados() + 1);
        
    }

    public void mostrarResultados() {
        System.out.println("Resultados del estudio de rayos en la zona: " + zona + " - " + descripcion + " (Estado: " + Estado + ")");
    }
 
}
