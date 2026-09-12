import java.util.ArrayList;

public class Area {
    
    private String nombre;
    private int numeroDeArea;
    private ArrayList<Empleado> empleados;

    public Area(String nombre) {
        this.nombre = nombre;
        this.empleados = new ArrayList<>();
    }

    public Area(int numeroDeArea) {
        this.numeroDeArea = numeroDeArea;
        this.empleados = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public int getNumeroDeArea() {
        return numeroDeArea;
    }

    public void agregarEmpleado(Empleado empleado) {
        empleados.add(empleado);
    }

    public void eliminarEmpleado(Empleado empleado) {
        empleados.remove(empleado);
    }

    public ArrayList<Empleado> getEmpleados() {
        return empleados;
    }

}
