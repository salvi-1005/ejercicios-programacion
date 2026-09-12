import java.util.ArrayList;
import java.util.Comparator;

public class Universidad {

    private String nombre;
    private ArrayList<Materia> materias;
    private ArrayList<Alumno> alumnosRegistrados;

    public Universidad(String nombre){
        this.nombre = nombre;
        this.materias = new ArrayList<>();
        this.alumnosRegistrados = new ArrayList<>();
    }

    public String getNombre(){
        return this.nombre;
    }

    public void setNombre(String nuevoNombre){
        this.nombre = nuevoNombre;
    }

    public ArrayList<Alumno> getAlumnosRegistrados(){
        return this.alumnosRegistrados;
    }

    public ArrayList<Materia> getMaterias(){
        return this.materias;
    }

    public Materia registrarMateria(Materia materia){
        materias.add(materia);
        return materia;
    }

    public Alumno registrarAlumno(Alumno alumno){
        alumnosRegistrados.add(alumno);
        return alumno;
    }

    public void inscribirAlumnoEnMateria(Alumno alumno, Materia materia){
        if (!getAlumnosRegistrados().contains(alumno)){
            System.out.println("el alumno " + alumno + " no esta inscripto en la universidad ");
            return;
        }
        if (!getMaterias().contains(materia)){
            System.out.println("la materia " + materia.getNombre() + " no existe en la universidad ");
            return;
        }
        if (materia.getAlumnosInscriptos().contains(alumno)){
            System.out.println("el alumno " + alumno.toString() + " ya esta inscripto en la materia " + materia.getNombre());
            return;
        }

        materia.inscribirAlumno(alumno);
    }

    public void mostrarMateriasDeUnAlumno(Alumno alumno){
        System.out.println("Materias de " + alumno + ": ");
        for (Materia materia : materias){
            if (materia.getAlumnosInscriptos().contains(alumno)){
                System.out.println(materia.getNombre());
            }
        }
    }

    public double calcularPromedioGeneral(){
        double sumaNotas = 0;
        if (alumnosRegistrados.isEmpty()){
            return 0;
        }
        for (Alumno alumno : alumnosRegistrados){
            sumaNotas += alumno.promedio();
        }
        double promedioGeneral = sumaNotas/alumnosRegistrados.size();
        return promedioGeneral;
        
    }

    public void mostrarAlumnosOrdenadosPorPromedio(){
        System.out.println("Alumnos ordenados por promedio: ");
        alumnosRegistrados.sort(Comparator.comparingDouble(Alumno::promedio).reversed());
        for (Alumno alumno : alumnosRegistrados) {
            System.out.println(alumno.toString());
        }
    }
    
}
