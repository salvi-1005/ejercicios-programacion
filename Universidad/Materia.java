import java.util.ArrayList;

public class Materia {

    private String nombre;
    private ArrayList<Alumno> alumnosInscriptos;

    public Materia(String nombre){
        this.nombre = nombre;
        this.alumnosInscriptos = new ArrayList<>();
    }

    public String getNombre(){
        return this.nombre;
    }

    public void setNombre(String nuevoNombre){
        this.nombre = nuevoNombre;
    }

    public ArrayList<Alumno> getAlumnosInscriptos(){
        return alumnosInscriptos;
    }


    public void inscribirAlumno(Alumno alumno){
        alumnosInscriptos.add(alumno);
    }

}
