public abstract class Estudio {

    protected String nombre;
    protected String descripcion;
    protected boolean Estado;

    public Estudio(String nombre, String descripcion) {
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.Estado = false;
    }

    public String getNombre() {
        return nombre;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public boolean getEstado() {
        return Estado;
    }

    public abstract void realizarEstudio(Paciente p);

    public abstract void mostrarResultados();

    
}
