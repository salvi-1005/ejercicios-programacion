public class Inscripcion {

    private Alumno alumno;
    private Materia materia;

    public Inscripcion(Alumno alumno, Materia materia){
        this.alumno = alumno;
        this.materia = materia;
    }

    public Alumno getAlumno(){
        return this.alumno;
    }

    public Materia getMateria(){
        return this.materia;
    }
    
}
