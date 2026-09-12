public class Donante {

    private String nombre;
    private String apellido;
    private int id;
    

    public Donante(String nombre, String apellido){
        this.nombre = nombre;
        this.apellido = apellido;
        this.id = 0; //Se le asigna un ID luego de ser registrado en la organización, para evitar que se asignen IDs a donantes que no han sido registrados.
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String toString(){
        return "(" + id + ")" + " " + apellido + ", " + nombre;
    }
    
}
