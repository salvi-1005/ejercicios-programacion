public class Empleado {
    
    private String nombre;
    private String apellido;
    private int numeroDeEmpleado;
    private Area area;

    public Empleado(String nombre, String apellido, int numeroDeEmpleado) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.numeroDeEmpleado = numeroDeEmpleado;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public int getNumeroDeEmpleado() {
        return numeroDeEmpleado;
    }

    public Area getArea() {
        return area;
    }

    public void setArea(Area area) {
        this.area = area;
    }

    public void bajarArea() {
        this.area = null;
    }

    @Override
    public String toString() {
        return nombre + " " + apellido;
    }

}
