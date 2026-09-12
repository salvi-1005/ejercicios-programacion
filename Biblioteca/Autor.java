import java.time.LocalDate;

public class Autor {

    private String nombre;
    private String apellido;
    private LocalDate fechaDeNacimiento;

    public Autor(String nombre, String apellido, LocalDate fechaDeNacimiento){
        this.nombre = nombre;
        this.apellido = apellido;
        this.fechaDeNacimiento = fechaDeNacimiento;
    }

    public String getNombre(){
        return this.nombre;
    }

    public void setNombre(String nuevoNombre){
        this.nombre = nuevoNombre;
    }

    public String getApellido(){
        return this.apellido;
    }

    public void setApellido(String nuevoApellido){
        this.nombre = nuevoApellido;
    }

    public LocalDate getFechaDeNacimiento(){
        return this.fechaDeNacimiento;
    }

    public void setFechaDeNacimiento(LocalDate nuevoFecha){
        this.fechaDeNacimiento = nuevoFecha;
    }

    public String toString(){
        return (nombre + " " + apellido);
    }
    
}
