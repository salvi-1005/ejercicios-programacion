public class Profesional {
    
    private int matricula;
    private String nombre;

    public Profesional(int matricula, String nombre) {
        this.matricula = matricula;
        this.nombre = nombre;
    }

    public int getMatricula() {
        return matricula;
    }

    public String getNombre() {
        return nombre;
    }

    public void recibirResultados(Receta receta) {
        System.out.println("Profesional " + nombre + " ha recibido los resultados de la receta con ID: " + receta.getIdentificador());
    }

}
