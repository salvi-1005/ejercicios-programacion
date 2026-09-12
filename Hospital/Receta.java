import java.util.ArrayList;

public class Receta {

    private int identificador;
    private ArrayList<Estudio> estudios;
    private Profesional profesional;
    private Paciente paciente;
    private boolean procesada;

    public Receta(int identificador, Profesional profesional, Paciente paciente, ArrayList<Estudio> estudios) {
        this.identificador = identificador;
        this.profesional = profesional;
        this.paciente = paciente;
        this.estudios = estudios;
        this.procesada = false;
    }

    public int getIdentificador() {
        return identificador;
    }

    public Profesional getProfesional() {
        return profesional;
    }

    public Paciente getPaciente() {
        return paciente;
    }

    public ArrayList<Estudio> getEstudios() {
        return estudios;
    }

    public boolean isProcesada() {
        return procesada;
    }

    public void procesar() {
        this.procesada = true;
    }

    public void mostrarReceta() {
        System.out.println("Receta ID: " + identificador);
        System.out.println("Profesional: " + profesional.getNombre());
        System.out.println("Paciente: " + paciente.getNombre());
        System.out.println("Estudios incluidos:");
        for (Estudio estudio : estudios) {
            System.out.println("- " + estudio.getNombre() + ": " + estudio.getDescripcion());
        }
    }

}
