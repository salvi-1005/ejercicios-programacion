public class Paciente {

    private int dni;
    private String nombre;
    private int cantEstudiosRealizados;

    public Paciente(int dni, String nombre) {
        this.dni = dni;
        this.nombre = nombre;
        this.cantEstudiosRealizados = 0;
    }

    public int getDni() {
        return dni;
    }

    public String getNombre() {
        return nombre;
    }

    public int getCantEstudiosRealizados() {
        return cantEstudiosRealizados;
    }

    public void setCantEstudiosRealizados(int cantEstudiosRealizados) {
        this.cantEstudiosRealizados = cantEstudiosRealizados;
    }

    public void recibirResultados(Receta receta) {
        System.out.println("Paciente " + nombre + " ha recibido los resultados de la receta con ID: " + receta.getIdentificador());
    }

    public boolean tieneAlMenosTresEstudios() {
        return cantEstudiosRealizados >= 3;
    }
    
}
