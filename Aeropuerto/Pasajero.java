public class Pasajero {

    private String nombre;
    private String apellido;
    private int dni;
    
    public Pasajero(String nombre, String apellido, int dni){
        this.nombre = nombre;
        this.apellido = apellido;
        this.dni = dni;
    }

    public String getNombre(){
        return this.nombre;
    }

    public String getApellido(){
        return this.apellido;
    }

    public int getDni(){
        return this.dni;
    }

    public String toString(){
        return (nombre + " " + apellido + " DNI: " + dni);
    }

}
