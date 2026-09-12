public class Main{
    public static void main(String[] args){
        Empleado e = new Empleado(6, "Santiago");
        System.out.println(e.getNumero());
        System.out.println(e.getNombre());
        e.setNumero(1053);
        e.setNombre("Salvador");
        e.verDatos();
    }
}