class Empleado extends Persona {
    private double salario;

    public Empleado(String nombre, int edad, double salario) {
        super(nombre, edad);
        this.salario = salario;
    }

    public double getSalario() {
        return salario;
    }

    @Override
    public void mostrarDatos() {
        super.mostrarDatos();
        System.out.println("Salario: " + salario);
    }
}
