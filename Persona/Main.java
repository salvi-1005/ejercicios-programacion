public class Main {
    public static void main(String[] args) {
        Persona p = new Persona("Salvador", 22);
        Estudiante es = new Estudiante("Pablo", 24, "LCD");
        Empleado em = new Empleado("Jose", 30, 100000);

        p.mostrarDatos();
        es.mostrarDatos();
        em.mostrarDatos();

    }
}
