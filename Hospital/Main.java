import java.util.ArrayList;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {

        //Crear nuevo hospital
        Hospital hospital = new Hospital("Pura Salud");
        
        //Registrar tres profesionales
        Profesional profesional1 = new Profesional(12345, "Dr. Juan Perez");
        Profesional profesional2 = new Profesional(67890, "Dra. Maria Gomez");
        Profesional profesional3 = new Profesional(33333, "Dr. Jose Mujica"); // Mismo número de matrícula que profesional1
 
        hospital.registrarProfesional(profesional1);
        hospital.registrarProfesional(profesional2);
        hospital.registrarProfesional(profesional3); 
        
        //Registrar tres pacientes
        Paciente paciente1 = new Paciente(11111111, "Carlos Sanchez");
        Paciente paciente2 = new Paciente(22222222, "Ana Rodriguez");
        Paciente paciente3 = new Paciente(33333333, "Lucia Fernandez"); // Mismo DNI que paciente1

        hospital.registrarPaciente(paciente1);
        hospital.registrarPaciente(paciente2);
        hospital.registrarPaciente(paciente3);

        Estudio estudio1 = new Rayos("Análisis de sangre", "Examen completo de sangre", "Abdomen");
        Estudio estudio2 = new Laboratorio("Radiografía de tórax", "Imagen del tórax para evaluar los pulmones", 3);
        Estudio estudio3 = new Rayos("Ecografía abdominal", "Evaluación de órganos abdominales", "Abdomen");

        //Cargar cinco recetas
        Receta receta1 = new Receta(1, profesional1, paciente1, new ArrayList<>(Arrays.asList(estudio2)));
        Receta receta2 = new Receta(2, profesional2, paciente2, new ArrayList<>(Arrays.asList(estudio2)));
        Receta receta3 = new Receta(3, profesional1, paciente1, new ArrayList<>(Arrays.asList(estudio3)));
        Receta receta4 = new Receta(4, profesional2, paciente2, new ArrayList<>(Arrays.asList(estudio1, estudio2)));
        Receta receta5 = new Receta(5, profesional1, paciente1, new ArrayList<>(Arrays.asList(estudio1, estudio2, estudio3)));

        hospital.cargarReceta(receta1);
        hospital.cargarReceta(receta2);
        hospital.cargarReceta(receta3);
        hospital.cargarReceta(receta4);
        hospital.cargarReceta(receta5);

        //Procesar las primeras 4 recetas
        hospital.procesarReceta(receta1);
        hospital.procesarReceta(receta2);
        hospital.procesarReceta(receta3);
        hospital.procesarReceta(receta4);

        estudio1.realizarEstudio(paciente1);
        estudio2.realizarEstudio(paciente1);
        estudio3.realizarEstudio(paciente1);

        ArrayList<Receta> recetas = new ArrayList<>();
        recetas.add(receta1);
        recetas.add(receta2);
        recetas.add(receta3);
        recetas.add(receta4);
        recetas.add(receta5);


        //Mostrar todas las recetas
        for (Receta receta : recetas) {
            receta.mostrarReceta();
        }

        //Mostrar recetas procesadas
        hospital.mostrarRecetasProcesadas();

        

        System.out.println("Cantidad de estudios realizados por " + paciente1.getNombre() + ": " + paciente1.getCantEstudiosRealizados());

        // Mostrar pacientes con al menos tres estudios realizados
        hospital.mostrarPacientesConAlMenosTresEstudios();
    }
}
