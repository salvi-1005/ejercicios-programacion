import java.util.ArrayList;

public class Hospital {
    
    private String nombre;
    private ArrayList<Profesional> profesionales;
    private ArrayList<Paciente> pacientes;
    private ArrayList<Receta> recetasCargadas;
    private ArrayList<Receta> recetasProcesadas;

    public Hospital(String nombre) {
        this.nombre = nombre;
        this.profesionales = new ArrayList<>();
        this.pacientes = new ArrayList<>();
        this.recetasCargadas = new ArrayList<>();
        this.recetasProcesadas = new ArrayList<>();
    }

    public String getNombre() {
        return nombre;
    }

    public void registrarProfesional(Profesional profesional) {
        for (Profesional p : profesionales) {
            if (p.getMatricula() == profesional.getMatricula()) {
                System.out.println("El profesional con matrícula " + profesional.getMatricula() + " ya está registrado.");
                return;
            }
        }
        this.profesionales.add(profesional);
    }

    public void registrarPaciente(Paciente paciente) {
        for (Paciente p : pacientes) {
            if (p.getDni() == paciente.getDni()) {
                System.out.println("El paciente con DNI " + paciente.getDni() + " ya está registrado.");
                return;
            }
        }
        this.pacientes.add(paciente);
    }

    public void cargarReceta(Receta receta) {
        for (Receta r : recetasCargadas) {
            if (r.getIdentificador() == receta.getIdentificador()) {
                System.out.println("La receta con ID: " + receta.getIdentificador() + " ya está cargada en el hospital.");
                return;
            }
        }
        this.recetasCargadas.add(receta);
        System.out.println("Disponible para procesar.");
    }

    public void procesarReceta(Receta receta) {
        if (recetasProcesadas.contains(receta) && receta.isProcesada()) {
            System.out.println("La receta con ID: " + receta.getIdentificador() + " ya ha sido procesada.");
            return;
        }
        if (recetasCargadas.contains(receta)) {
            System.out.println("Procesando receta con ID: " + receta.getIdentificador());
            this.recetasProcesadas.add(receta);
            this.recetasCargadas.remove(receta);
            for (Estudio estudio : receta.getEstudios()) {
                estudio.realizarEstudio(receta.getPaciente());
            }
            receta.procesar();
        } else {
            System.out.println("La receta con ID: " + receta.getIdentificador() + " no está cargada en el hospital.");
        }
    }

    public void enviarResultadosAlProfesional(Receta receta) {
        if (!recetasProcesadas.contains(receta)) {
            System.out.println("La receta con ID: " + receta.getIdentificador() + " no ha sido procesada aún.");
            return;
        }
        for (Estudio estudio : receta.getEstudios()) {
            estudio.mostrarResultados();
        }
        receta.getProfesional().recibirResultados(receta);
    }

    public void enviarResultadosAlPaciente(Receta receta) {
        if (!recetasProcesadas.contains(receta)) {
            System.out.println("La receta con ID: " + receta.getIdentificador() + " no ha sido procesada aún.");
            return;
        }
        for (Estudio estudio : receta.getEstudios()) {
            estudio.mostrarResultados();
        }
        receta.getPaciente().recibirResultados(receta);
    }

    public void mostrarRecetasProcesadas() {
        System.out.println("Recetas procesadas en el hospital " + nombre + ":");
        for (Receta receta : recetasProcesadas) {
            receta.mostrarReceta();
        }
    }

    public void mostrarPacientesConAlMenosTresEstudios() {
        System.out.println("Pacientes con al menos tres estudios realizados en el hospital " + nombre + ":");
        for (Paciente paciente : pacientes) {
            if (paciente.tieneAlMenosTresEstudios()) {
                System.out.println("- " + paciente.getNombre() + " (DNI: " + paciente.getDni() + ")");
            }
        }
    }

}
