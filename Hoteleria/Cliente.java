public class Cliente {

    private String nombre;
    private String apellido;
    private String numeroDeTelefono;
    private String correoElectronico;
    private Habitacion habitacion;


    public Cliente(String nombre, String apellido, String numeroDeTelefono, String correoElectronico) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.numeroDeTelefono = numeroDeTelefono;
        this.correoElectronico = correoElectronico;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public String getNumeroDeTelefono() {
        return numeroDeTelefono;
    }

    public String getCorreoElectronico() {
        return correoElectronico;
    }

    public Habitacion getHabitacion() {
        return habitacion;
    }

    public void asignarHabitacion(Habitacion habitacion) {
        this.habitacion = habitacion;
    }

    public void liberarHabitacion() {
        this.habitacion = null;
    }
    
}
