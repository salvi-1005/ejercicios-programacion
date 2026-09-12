import java.util.ArrayList;
import java.util.Arrays;

public class Main {

    public static void main(String[] args){

        Universidad universidad = new Universidad("UNSAM");

        Alumno alumno1 = universidad.registrarAlumno(new Alumno("Salvador", "Dangelo", 1053, new ArrayList<>(Arrays.asList(8.75, 9.75, 7.00))));
        Alumno alumno2 = universidad.registrarAlumno(new Alumno("Gianfranco", "Desirello", 1134, new ArrayList<>(Arrays.asList(7.00, 9.50, 6.25))));
        Alumno alumno3 = universidad.registrarAlumno(new Alumno("Franco", "Ditale", 1245, new ArrayList<>(Arrays.asList(5.75, 7.75, 8.00))));

        Materia materia1 = universidad.registrarMateria(new Materia("Matematica Discreta"));
        Materia materia2 = universidad.registrarMateria(new Materia("Probabilidad y Estadistica"));
        Materia materia3 = universidad.registrarMateria(new Materia("Algoritmos 1"));

        universidad.inscribirAlumnoEnMateria(alumno1, materia1);
        universidad.inscribirAlumnoEnMateria(alumno2, materia2);
        universidad.inscribirAlumnoEnMateria(alumno3, materia3);

        universidad.mostrarMateriasDeUnAlumno(alumno1);
        universidad.mostrarMateriasDeUnAlumno(alumno2);
        universidad.mostrarMateriasDeUnAlumno(alumno3);

        System.out.println("Promedio general de UNSAM: " + universidad.calcularPromedioGeneral());

        universidad.mostrarAlumnosOrdenadosPorPromedio();

        //Trato de inscribir a un alumno en una materia sin estar registrado en la universidad
        Alumno alumno4 =  new Alumno("Thiago", "Sosa", 1265, new ArrayList<>(Arrays.asList(6.75, 7.75, 10.00)));

        universidad.inscribirAlumnoEnMateria(alumno4, materia3);

        //Trato de inscribir a un alumno en una materia que no existe en la universidad
        Materia materia4 = new Materia("Analisis Avanzado");
        universidad.inscribirAlumnoEnMateria(alumno3, materia4);

        //Trato de inscribir a un alumno que ya está inscripto en una materia
        universidad.inscribirAlumnoEnMateria(alumno1, materia1);


    }
    
}
