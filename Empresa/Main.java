public class Main {
    
    public static void main(String[] args) {
        
        Area area1 = new Area("Recursos Humanos");
        Area area2 = new Area("Tecnología");

        Empresa empresa = new Empresa();
        
        empresa.agregarArea(area1);
        empresa.agregarArea(area2);

        Empleado empleado1 = new Empleado("Juan", "Pérez", 123);
        Empleado empleado2 = new Empleado("María", "Gómez", 456);

        empleado1.setArea(area1);
        empleado2.setArea(area2);

        empresa.registrarEmpleado(empleado1);
        empresa.registrarEmpleado(empleado2);

        System.out.println("Área de Juan: " + empresa.obtenerAreaDeUnEmpleado(empleado1).getNombre());
        System.out.println("Área de María: " + empresa.obtenerAreaDeUnEmpleado(empleado2).getNombre());

        empresa.transferirEmpleado(empleado1, area2);
        System.out.println("Área de Juan después de la transferencia: " + empresa.obtenerAreaDeUnEmpleado(empleado1).getNombre());

        empresa.eliminarEmpleado(empleado2);
        System.out.println("Área de María después de eliminarla: " + empresa.obtenerAreaDeUnEmpleado(empleado2));
        
        System.out.println("empleados de Tecnología: " + area2.getEmpleados());
    }
}
