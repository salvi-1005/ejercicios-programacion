import java.util.ArrayList;

public class Empresa {
    
    private ArrayList<Area> areas;

    public Empresa() {
        this.areas = new ArrayList<>();
    }

    public Area obtenerAreaDeUnEmpleado(Empleado empleado) {
        if (empleado.getArea() == null) {
            return null;
        }
        return empleado.getArea();
    }

    
    private boolean contieneArea(Area area) {
        return areas.contains(area);
    }


    public void registrarEmpleado(Empleado empleado) {
        Area area = empleado.getArea();

        if (area != null && contieneArea(area)) {
            area.agregarEmpleado(empleado);
        } else {
            System.out.println("El área no pertenece a la empresa");
        }
    }

    public void transferirEmpleado(Empleado empleado, Area nuevaArea) {
        
        if (!contieneArea(nuevaArea)) {
            System.out.println("El área destino no pertenece a la empresa");
            return;
        }

        Area areaActual = empleado.getArea();
        if (areaActual != null) {
            areaActual.eliminarEmpleado(empleado);
        }
        nuevaArea.agregarEmpleado(empleado);
        empleado.setArea(nuevaArea);
    }

    public void eliminarEmpleado(Empleado empleado) {
        Area area = empleado.getArea();
        if (area != null) {
            area.eliminarEmpleado(empleado);
        }
        empleado.bajarArea();
        empleado.setArea(null);
    }

    public void agregarArea(Area area) {
        if (!contieneArea(area)) {
            areas.add(area);
        } else {
            System.out.println("El área ya existe en la empresa");
        }
    }
    

}
